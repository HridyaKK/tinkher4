from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    crime_score = Column(Integer, nullable=False)
    lighting_score = Column(Integer, nullable=False)
    crowd_score = Column(Integer, nullable=False)

    night_flag = Column(Boolean, default=False)