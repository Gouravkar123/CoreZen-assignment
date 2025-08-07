from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base
from .enums import TransactionType


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    available_quantity = Column(Integer)

    transactions = relationship("StockTransaction", back_populates="product")


class StockTransaction(Base):
    __tablename__ = "stock_transactions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    transaction_type = Column(Enum(TransactionType))
    timestamp = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product", back_populates="transactions")
