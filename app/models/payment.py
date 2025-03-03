import uuid
from sqlalchemy import ForeignKey, Column, String, Numeric # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"
    
    paymentuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    appointmentuuid = Column(UUID(as_uuid=True), ForeignKey("appointments.appointmentuuid"), nullable=False)
    paymentamount = Column(Numeric(10, 2), nullable=False)
    paymentmethod = Column(String, nullable=False)
    statusuuid = Column(UUID(as_uuid=True), ForeignKey("payment_status.statusuuid"), nullable=False)
    
    appointment = relationship("Appointment")
    status = relationship("PaymentStatus", back_populates="payments")
