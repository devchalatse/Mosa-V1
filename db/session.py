from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@giveflow_db:5432/dbname"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # optional, shows SQL logs
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
