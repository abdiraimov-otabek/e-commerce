from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db import get_database_url
from app import crud, schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[schemas.CategoryOut])
async def list_categories(db: AsyncSession = Depends(get_database_url)):
    """Barcha kategoriyalar (asosiy + sublar bilan)"""
    return await crud.get_all_categories(db)

@router.get("/{category_id}", response_model=schemas.CategoryOut)
async def get_category(category_id: int, db: AsyncSession = Depends(get_database_url)):
    category = await crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=schemas.CategoryOut)
async def create_category(category: schemas.CategoryCreate, db: AsyncSession = Depends(get_database_url)):
    return await crud.create_category(db, category)

@router.put("/{category_id}", response_model=schemas.CategoryOut)
async def update_category(category_id: int, data: schemas.CategoryUpdate, db: AsyncSession = Depends(get_database_url)):
    category = await crud.update_category(db, category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}")
async def delete_category(category_id: int, db: AsyncSession = Depends(get_database_url)):
    category = await crud.delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"status": "deleted"}
