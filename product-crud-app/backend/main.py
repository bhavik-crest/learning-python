from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from math import ceil

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ideally replace with frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products", response_model=schemas.PaginatedProducts)
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str = Query("", max_length=100),
    db: Session = Depends(get_db),
):
    # 1. Count *after* search is applied
    total = crud.count_products(db, search)

    # 2. Calculate pagination
    pages = max(ceil(total / limit), 1)
    page  = min(page, pages) 
    skip  = (page - 1) * limit

    # 3. Fetch the slice
    items = crud.get_products(db, skip=skip, limit=limit, search=search)

    # 4. Return metadata + items
    return {
        "total": total,
        "page":  page,
        "limit": limit,
        "pages": pages,
        "items": items,
    }

@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)
