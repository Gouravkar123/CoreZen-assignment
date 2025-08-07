from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import async_session
from collections.abc import AsyncGenerator

router = APIRouter(prefix="/stock", tags=["Stock"])

# Async Dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@router.post("/", response_model=schemas.StockTransactionOut)
async def create_stock_transaction(
    transaction: schemas.StockTransactionCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_transaction(db, transaction)


@router.get("/", response_model=list[schemas.StockTransactionOut])
async def list_all_transactions(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_all_transactions(db, skip=skip, limit=limit)


@router.get("/product/{product_id}", response_model=list[schemas.StockTransactionOut])
async def transactions_by_product(
    product_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_transactions_by_product(db, product_id, skip=skip, limit=limit)
