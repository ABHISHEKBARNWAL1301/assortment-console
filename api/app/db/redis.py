# Async Redis Conn
# import aioredis
# from app.settings import settings

# redis_db = aioredis.from_url(
#     f'redis://{settings.postgres_service}:{settings.redis_port}/{settings.redis_db}'
# )


# Sync redis connection
import redis
from app.config import settings

# Adjust the connection details as needed
redis_db = redis.Redis(
    host=settings.redis_service, port=settings.redis_port, db=settings.redis_db, decode_responses=True
)
