import uuid
from sqlalchemy import ForeignKey, Column, String # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    useruuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    username = Column(String(50), nullable=False)
    useremail = Column(String(50), unique=True, nullable=False, index=True)
    userpass = Column(String, nullable=False)
    roleuuid = Column(UUID(as_uuid=True), ForeignKey("roles.roleuuid"), nullable=False)

    role = relationship("Role", back_populates="users")
    staff = relationship("Staff", uselist=False, back_populates="user")
