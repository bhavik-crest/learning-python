from sqlalchemy import or_, cast, String
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.product import Product                     # SQLAlchemy model
from schemas.product import ProductCreate              # Pydantic schema


# ---------------------------------------------------------------------------
# Helper: build a query with optional search filter
# ---------------------------------------------------------------------------
def _filtered_query(db: Session, search: str | None = None):
    q = db.query(Product)
    if search:
        pattern = f"%{search}%"
        q = q.filter(
            or_(
                Product.name.ilike(pattern),
                Product.description.ilike(pattern),
                cast(Product.price, String).ilike(pattern),   # search price too
            )
        )
    return q


# ---------------------------------------------------------------------------
# Count products (after search filter)
# ---------------------------------------------------------------------------
def count_products(db: Session, search: str | None = None) -> int:
    return _filtered_query(db, search).count()


# ---------------------------------------------------------------------------
# List products with pagination
# ---------------------------------------------------------------------------
def get_products(
    db: Session,
    skip: int,
    limit: int,
    search: str | None = None,
):
    return (
        _filtered_query(db, search)
        .order_by(Product.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


# ---------------------------------------------------------------------------
# Fetch single product
# ---------------------------------------------------------------------------
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# ---------------------------------------------------------------------------
# Create product
# ---------------------------------------------------------------------------
def create_product(db: Session, payload: ProductCreate):
    db_product = Product(**payload.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# ---------------------------------------------------------------------------
# Update product
# ---------------------------------------------------------------------------
def update_product(db: Session, product_id: int, payload: ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in payload.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


# ---------------------------------------------------------------------------
# Delete product
# ---------------------------------------------------------------------------
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "code": "PRODUCT_NOT_FOUND",
                "message": f"Product with ID {product_id} not found",
            },
        )

    db.delete(db_product)
    db.commit()
    return {
        "code": "PRODUCT_DELETED",
        "message": f"Product {product_id} deleted successfully",
    }