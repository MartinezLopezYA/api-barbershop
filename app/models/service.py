import uuid
from sqlalchemy import ForeignKey, Column, String, Numeric # type: ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from app.core.database import Base

class Service(Base):
    __tablename__ = "services"
    
    serviceuuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    servicename = Column(String(50), nullable=False)
    serviceprice = Column(Numeric(10, 2), nullable=False)
    categoryuuid = Column(UUID(as_uuid=True), ForeignKey("categories.categoryuuid"), nullable=False)
    
    category = relationship("Category", back_populates="services")
    appointments = relationship("Appointment", back_populates="service")

