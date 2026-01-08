from fastapi import FastAPI
from app.api.routes import auth, documents
from app.core.database import engine
from app.models import user, document
from sqlalchemy import select
from app.models.user import User
from app.core.security import hash_password
app = FastAPI()

app.include_router(auth.router)
app.include_router(documents.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # create initial admin user if not exists
    from app.core.database import AsyncSessionLocal

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.email == "admin@example.com")
        )
        user = result.scalar_one_or_none()

        if not user:
            admin = User(
                email="admin@example.com",
                hashed_password=hash_password("admin123")
            )
            session.add(admin)
            await session.commit()

