from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.db_config import DB_CONFIG

DATABASE_URL = (
    f"mysql+pymysql://{DB_CONFIG['user']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)