import uuid
from sqlalchemy import ForeignKey, Column, String # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Role(Base):
    __tablename__ = "roles"
    
    roleuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    rolename = Column(String(50), unique=True, nullable=False)
    
    users = relationship("User", back_populates="role")
