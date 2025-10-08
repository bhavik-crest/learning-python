from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.crud.user import create_user, get_user_by_email, authenticate_user
from app.database import get_db
from app.core.security import create_access_token, get_current_user
from app.auth.token_blacklist import is_token_blacklisted, add_token_to_blacklist

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_users_me(current_user=Depends(get_current_user)):
    return current_user


@router.post("/logout")
def logout(authorization: str = Header(...)):
    # Authorization header is expected as 'Bearer <token>'
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid authorization header")

    token = authorization.split(" ")[1]
    add_token_to_blacklist(token)
    return {"msg": "Logged out successfully"}
