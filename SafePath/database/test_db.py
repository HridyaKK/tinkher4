from database.connection import SessionLocal
from database.models import Area

def test_db():
    session = SessionLocal()

    new_area = Area(
        name="MG Road",
        latitude=12.9750,
        longitude=77.6050,
        crime_score=20,
        lighting_score=80,
        crowd_score=70,
        night_flag=False
    )

    session.add(new_area)
    session.commit()

    areas = session.query(Area).all()

    for area in areas:
        print(area.name, area.crime_score)

    session.close()

if __name__ == "__main__":
    test_db()