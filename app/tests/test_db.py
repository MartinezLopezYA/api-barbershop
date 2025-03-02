import asyncio
from sqlalchemy import text  # type: ignore
from app.core.database import engine

async def test_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

asyncio.run(test_connection())
