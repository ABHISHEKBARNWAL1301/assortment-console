# Importing necessary modules and classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Product
from app.config import settings

# Sync connection setup for PostgreSQL
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

# Creating a SQLAlchemy engine for PostgreSQL
postgres_engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating a session maker for PostgreSQL with certain configurations
Session = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)

# Creating a synchronous database session
postgres_sync_db = Session()


async def init_postgres_db():
    # Creating the 'Product' table in the PostgreSQL database
    Product.__table__.create(bind=postgres_engine, checkfirst=True)
    
    # Printing a message indicating that the table has been created
    print("Postgres table created")
