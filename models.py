# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class License(Base):
    __tablename__ = 'licenses'
    id = Column(Integer, primary_key=True)
    license_key = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    user_email = Column(String(120))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Trial(Base):
    __tablename__ = 'trials'
    id = Column(Integer, primary_key=True)
    user_email = Column(String(120), unique=True, nullable=False)
    trial_start = Column(DateTime, default=datetime.datetime.utcnow)
    trial_end = Column(DateTime)
