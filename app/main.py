# app/main.py
from fastapi import FastAPI
from app.routers import product, stock
from app.init_db import init_db  # NEW

app = FastAPI(title="Inventory Management API")

@app.on_event("startup")
async def startup():
    await init_db()  # CREATE TABLES

app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(stock.router, prefix="/stock", tags=["Stock"])

@app.get("/")
def root():
    return {"message": "Welcome to Inventory Management API"}
