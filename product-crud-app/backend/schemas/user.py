from pydantic import BaseModel, EmailStr, ConfigDict

class _Config:
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 equivalent of orm_mode

# ── Shared fields ───────────────────────────────────────
class UserBase(BaseModel):
    email: EmailStr
    model_config = _Config.model_config

# ── For registration ────────────────────────────────────
class UserCreate(UserBase):
    password: str

# ── For login payload ───────────────────────────────────
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    model_config = _Config.model_config

# ── Response back to frontend ───────────────────────────
class UserOut(UserBase):
    id: int