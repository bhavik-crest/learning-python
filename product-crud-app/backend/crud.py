from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status
import models, schemas

# helper so we don’t repeat the same “apply search” code twice
def _filtered_query(db: Session, search: str | None = None):
    q = db.query(models.Product)
    if search:
        pattern = f"%{search}%"
        # Search in name OR description
        q = q.filter(
            or_(
                models.Product.name.ilike(pattern),
                models.Product.description.ilike(pattern),
                models.Product.price.ilike(pattern),
            )
        )
    return q

# count products
def count_products(db: Session, search: str | None = None) -> int:
    return _filtered_query(db, search).count()

# Get products with pagination
def get_products(db: Session, skip: int, limit: int, search: str | None = None):
    return _filtered_query(db, search).order_by(models.Product.id.desc()).offset(skip).limit(limit).all()

# Get product by ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

# Create product
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Update product
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

# Delete product
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        # identical envelope to the one in get_product
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
    
    #return db_product
