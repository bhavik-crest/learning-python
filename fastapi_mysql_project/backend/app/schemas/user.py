from pydantic import BaseModel, EmailStr, ConfigDict, validator

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    password: str
    profile_photo: str | None = None

    @validator('password')
    def validate_password_length(cls, value):
        max_len = 72
        if len(value.encode('utf-8')) > max_len:
            raise ValueError(f"Password cannot be longer than {max_len} bytes")
        return value

class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: str
    profile_photo: str | None = None

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
