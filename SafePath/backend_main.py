from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List
from database.connection import SessionLocal
from database.models import Area
from sqlalchemy.orm import Session
from fastapi import Depends
from database.models import EmergencyReport as EmergencyReportModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SafePath API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AreaSchema(BaseModel):
    name: str
    lat: float
    lon: float
    crime: int
    lighting: int
    crowd: int
    night: int


class EmergencyReport(BaseModel):
    location: str
    issue: str


# ----------------------------
# Safety Score Logic
# ----------------------------

def calculate_safety_score(area: Area):
    crime_weight = 0.4
    lighting_weight = 0.2
    crowd_weight = 0.2
    night_penalty = 15 if area.night == 1 else 0

    score = (
        (100 - area.crime) * crime_weight +
        area.lighting * lighting_weight +
        area.crowd * crowd_weight
    ) - night_penalty

    return int(score)


# ----------------------------
# Routes
# ----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "SafePath Backend Running"}

@app.get("/areas")
def get_areas(db: Session = Depends(get_db)):

    areas = db.query(Area).all()

    response = []

    for area in areas:
        score = calculate_safety_score(area)

        response.append({
            "id": area.id,
            "name": area.name,
            "lat": area.lat,
            "lon": area.lon,
            "safety_score": score
        })

    return response

@app.post("/report")
def create_report(report: EmergencyReport, db: Session = Depends(get_db)):

    new_report = EmergencyReportModel(
        location=report.location,
        issue=report.issue
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return {"message": "Report stored successfully"}


@app.get("/reports")
def get_reports(db: Session = Depends(get_db)):

    reports = db.query(EmergencyReportModel).all()

    return [
        {
            "id": r.id,
            "location": r.location,
            "issue": r.issue,
            "time": r.time.strftime("%d %b %Y - %I:%M %p")
        }
        for r in reports
    ]

