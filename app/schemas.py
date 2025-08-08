from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


# Enum for Stock Transaction Type

class TransactionType(str, Enum):
    IN = "IN"
    OUT = "OUT"

# Product Schemas

class ProductBase(BaseModel):
    name: str
    description: str
    price: float = Field(..., ge=0, description="Price must be non-negative")
    available_quantity: int = Field(..., ge=0, description="Quantity must be non-negative")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True


# Stock Transaction Schemas


class StockTransactionBase(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1, description="Quantity must be at least 1")
    transaction_type: TransactionType

class StockTransactionCreate(StockTransactionBase):
    pass

class StockTransactionOut(StockTransactionBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
