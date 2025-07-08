from fastapi import FastAPI
from core.database import Base, engine
from routes import products, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

# CORS: Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include product routes
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(auth.router, prefix="/api/auth")