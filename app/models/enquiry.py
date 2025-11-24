from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class Enquiry(Base):
    __tablename__ = "enquiries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    option = Column(String, nullable=False)
    school_name = Column(String, nullable=True)
    city_state = Column(String, nullable=True)
    requirement = Column(String, nullable=True)
    query = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.now)
