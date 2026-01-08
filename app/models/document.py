from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.user import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
