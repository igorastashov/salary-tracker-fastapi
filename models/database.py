import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

# DB_USER = "astashovivl"
# DB_PASS = "WhTdQdMFTAxz8g05fz7CgPTr4jnKxB5b"
# DB_HOST = "dpg-cp1g06u3e1ms738l4no0-a.frankfurt-postgres.render.com"
# DB_NAME = "db_fastapi_6jhr"

# Load .env file
load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
