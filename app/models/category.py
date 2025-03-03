import uuid
from sqlalchemy import ForeignKey, Column, String # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"
    
    categoryuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    categoryname = Column(String(50), nullable=False, unique=True)
    
    services = relationship("Service", back_populates="category")
