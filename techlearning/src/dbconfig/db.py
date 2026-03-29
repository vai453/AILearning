from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
)
# Example:
# MySQL: mysql+pymysql://user:password@localhost:3306/mydb
# SQLite: sqlite:///mydb.db

# Create engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,        # number of permanent connections
    max_overflow=20,     # extra connections allowed above pool_size
    pool_timeout=30,     # wait time before giving connection error
    pool_recycle=1800,   # recycle connection after 30 minutes
    echo=False           # set True for SQL logs
)

# Session factory
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=engine,
        expire_on_commit=False
    )
)

# Base class for models
Base = declarative_base()
