from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  STEP 1 CREATE SQLALCHEMY ENGINE
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# connect to database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# connect to engine (ORM)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# class orm in sqlalchemy
Base = declarative_base()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()