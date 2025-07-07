from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)
