import hashlib
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        phone_number=user.phone_number,
        hashed_password=hashed_password,
        profile_photo=user.profile_photo,
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError as e:
        db.rollback()  # Rollback the session to make it usable again
        if "Duplicate entry" in str(e.orig):
            raise HTTPException(status_code=400, detail="User with this phone number already exists")
        else:
            raise HTTPException(status_code=400, detail="Failed to create user due to database error")
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user
