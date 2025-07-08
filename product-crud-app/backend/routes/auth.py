# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from crud import user as crud_user
from schemas.user import UserCreate, UserLogin, UserOut
from schemas.token import Token
from core.security import create_access_token, add_token_to_blacklist
from core.database import get_db

router = APIRouter()

@router.post("/register")
def register(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    if crud_user.get_user_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud_user.create_user(db, email=email, password=password)
    return user

@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud_user.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user.id, "email": user.email})
    return {"access_token": token, "token_type": "bearer", "user": user}

@router.post("/logout")
async def logout(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=400, content={"detail": "Authorization header missing or invalid"})

    token = auth_header.split(" ")[1]
    add_token_to_blacklist(token)
    return {"message": "Logout successful"}