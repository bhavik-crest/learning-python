from sqlalchemy.orm import Session
from models.user import User
from core.security import get_password_hash, verify_password

# ─────────────────────────────────────────────────────────
def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

# ─────────────────────────────────────────────────────────
def create_user(db: Session, email: str, password: str) -> User:
    hashed_password = get_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ─────────────────────────────────────────────────────────
def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None