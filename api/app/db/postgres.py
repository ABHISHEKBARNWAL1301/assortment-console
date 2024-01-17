import databases
from app.config import settings

# Async connection
SQLALCHEMY_DATABASE_URL_ASYNC = (
    "postgresql+asyncpg://"
    + settings.postgres_user
    + ":"
    + settings.postgres_password
    + "@"
    + settings.postgres_service
    + ":5432/"
    + settings.postgres_db
)

postgres_db = databases.Database(SQLALCHEMY_DATABASE_URL_ASYNC)



