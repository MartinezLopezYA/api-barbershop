import uuid
from sqlalchemy import ForeignKey, Column, String, Numeric, DateTime # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class AppointmentStatus(Base):
    __tablename__ = "appointment_status"
    
    statusuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    statusname = Column(String(50), unique=True, nullable=False)
    
    appointments = relationship("Appointment", back_populates="status")