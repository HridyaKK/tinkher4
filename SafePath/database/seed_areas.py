from database.connection import SessionLocal
from database.models import Area

def seed_data():
    db = SessionLocal()

    areas = [
        Area(name="MG Road", lat=12.975, lon=77.605, crime=30, lighting=70, crowd=60, night=50),
        Area(name="Indiranagar", lat=12.9719, lon=77.6412, crime=40, lighting=80, crowd=75, night=60),
        Area(name="Whitefield", lat=12.9698, lon=77.7500, crime=50, lighting=65, crowd=55, night=45),
    ]

    db.add_all(areas)
    db.commit()
    db.close()

    print("Areas seeded successfully!")

if __name__ == "__main__":
    seed_data()