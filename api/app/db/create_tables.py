from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import (Product)
from app.config import settings




# Sync connection
SQLALCHEMY_DATABASE_URL = (
    "postgresql://"
    + settings.postgres_user
    + ":"
    + settings.postgres_password
    + "@"
    + settings.postgres_service
    + ":5432/"
    + settings.postgres_db
)
postgres_engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)
postgres_sync_db = Session()


async def init_postgres_db():
    Product.__table__.create(bind=postgres_engine, checkfirst=True)
    print("Postgres table created")