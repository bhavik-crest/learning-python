from sqlalchemy import Column, Integer, String, Boolean
from core.database import Base  # ✅ Updated import path

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)             # ✅ Length & null safety
    description = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    image_url = Column(String(255), nullable=True)
    is_available = Column(Boolean, default=True)