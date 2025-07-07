from fastapi import FastAPI
from routes import products
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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