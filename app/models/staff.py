import uuid
from sqlalchemy import ForeignKey, Column, String # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Staff(Base):
    __tablename__ = "staff"
    
    staffuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    staffname = Column(String(50), nullable=False)  # barber, manicurist, etc.
    useruuid = Column(UUID(as_uuid=True), ForeignKey("users.useruuid"), nullable=False)
    
    user = relationship("User", back_populates="userstaff")
    appointments = relationship("Appointment", back_populates="staff")