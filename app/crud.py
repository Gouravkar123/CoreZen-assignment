from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from app import models, schemas
from datetime import datetime
from fastapi import HTTPException

async def create_transaction(db: AsyncSession, tx: schemas.StockTransactionCreate):
    result = await db.execute(
        select(models.Product).where(models.Product.id == tx.product_id)
    )
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if tx.transaction_type == "OUT" and product.available_quantity < tx.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")

    if tx.transaction_type == "IN":
        product.available_quantity += tx.quantity
    elif tx.transaction_type == "OUT":
        product.available_quantity -= tx.quantity

    stock_tx = models.StockTransaction(
        product_id=tx.product_id,
        quantity=tx.quantity,
        transaction_type=tx.transaction_type,
        timestamp=datetime.utcnow()
    )

    db.add(stock_tx)
    await db.commit()
    await db.refresh(stock_tx)
    return stock_tx


async def get_all_transactions(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(models.StockTransaction).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_transactions_by_product(db: AsyncSession, product_id: int, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(models.StockTransaction)
        .where(models.StockTransaction.product_id == product_id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()
