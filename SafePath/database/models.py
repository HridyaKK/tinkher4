from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    crime = Column(Integer, nullable=False)
    lighting = Column(Integer, nullable=False)
    crowd = Column(Integer, nullable=False)
    night = Column(Integer, nullable=False)


class EmergencyReport(Base):
    __tablename__ = "emergency_reports"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String(255), nullable=False)
    issue = Column(String(500), nullable=False)
    time = Column(DateTime, default=datetime.utcnow)