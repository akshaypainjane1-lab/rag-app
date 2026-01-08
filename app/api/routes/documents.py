from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.document import Document

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/")
async def create_document(
    title: str,
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_user)
):
    doc = Document(title=title, owner_id=user.id)
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    return doc
