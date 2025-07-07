from pydantic import BaseModel
from math import ceil
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    image_url: Optional[str] = None
    is_available: bool = True

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    name: str
    description: str
    price: int
    is_available: bool

    class Config:
        orm_mode = True

class PaginatedProducts(BaseModel):
    total: int          # total rows in table
    page: int           # current page (1‑based)
    limit: int          # page size
    pages: int          # total pages
    items: List[Product]