from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.category import Category

async def get_all_categories(db: AsyncSession):
    result = await db.execute(select(Category).filter(Category.parent_id == None))
    return result.scalars().unique().all()

async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).filter(Category.id == category_id))
    return result.scalar_one_or_none()

async def create_category(db: AsyncSession, data):
    new_category = Category(**data.model_dump())
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category

async def update_category(db: AsyncSession, category_id: int, data):
    category = await get_category(db, category_id)
    if not category:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(category, key, value)
    await db.commit()
    await db.refresh(category)
    return category

async def delete_category(db: AsyncSession, category_id: int):
    category = await get_category(db, category_id)
    if category:
        await db.delete(category)
        await db.commit()
    return category
