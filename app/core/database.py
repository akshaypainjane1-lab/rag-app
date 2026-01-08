from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://fastapi_tr4s_user:XKXxP2DKiEkKbdgRGnKW9RlM0pjxlUIW@dpg-d5fku5juibrs73du9q80-a.virginia-postgres.render.com/fastapi_tr4s"

engine = create_async_engine(
    DATABASE_URL,
    pool_size=20,        # important for concurrency
    max_overflow=10,
    future=True,
    echo=False
)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
