from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from math import ceil
from core.security import get_current_user

from core.database import get_db
from schemas.product import (
    ProductCreate,
    Product,            # response schema
    PaginatedProducts,
)
from crud import product as crud_product   # <— Alias for DB helpers

router = APIRouter()

# -------------------------------------------------------------------
# 1. LIST (with pagination + search)
# -------------------------------------------------------------------
@router.get("/", response_model=PaginatedProducts)
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str = Query(""),
    db: Session = Depends(get_db),
):
    total = crud_product.count_products(db, search)
    pages = max(ceil(total / limit), 1)
    page  = min(page, pages)            # clamp page if search shrank results
    skip  = (page - 1) * limit
    items = crud_product.get_products(db, skip, limit, search)

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "pages": pages,
        "items": items,
    }


# -------------------------------------------------------------------
# 2. GET BY ID
# -------------------------------------------------------------------
@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_product.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# -------------------------------------------------------------------
# 3. CREATE
# -------------------------------------------------------------------
@router.post("/", response_model=Product, status_code=201)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, payload)


# -------------------------------------------------------------------
# 4. UPDATE
# -------------------------------------------------------------------
@router.put("/{product_id}", response_model=Product)
def update_product(
    product_id: int,
    payload: ProductCreate,         # or ProductUpdate if you have one
    db: Session = Depends(get_db),
):
    updated = crud_product.update_product(db, product_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# -------------------------------------------------------------------
# 5. DELETE
# -------------------------------------------------------------------
@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud_product.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")