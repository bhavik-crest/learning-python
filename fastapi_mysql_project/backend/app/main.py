from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.api import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
