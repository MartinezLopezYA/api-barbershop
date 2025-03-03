import uuid
from sqlalchemy import ForeignKey, Column, String, DateTime # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Appointment(Base):
    __tablename__ = "appointments"
    
    appointmentuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    clientuuid = Column(UUID(as_uuid=True), ForeignKey("users.useruuid"), nullable=False)
    staffuuid = Column(UUID(as_uuid=True), ForeignKey("staff.staffuuid"), nullable=False)
    serviceuuid = Column(UUID(as_uuid=True), ForeignKey("services.serviceuuid"), nullable=False)
    statusuuid = Column(UUID(as_uuid=True), ForeignKey("appointment_status.statusuuid"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    
    client = relationship("User")
    staff = relationship("Staff", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
    status = relationship("AppointmentStatus", back_populates="appointments")
