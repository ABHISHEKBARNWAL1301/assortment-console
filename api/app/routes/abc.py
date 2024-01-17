import json
from datetime import datetime
from fastapi import APIRouter
from sqlalchemy import select
from app.models import Product
from app.db import postgres_db, redis_db

abc = APIRouter(prefix="/couture/search", tags=["analytics"])


@abc.get("/products", operation_id="fetch-analytics-info")
async def fetch_analytics_info(
    start: str,
    end: str,
):
    cache_key = f"analytics:{start}:{end}"
    response = redis_db.get(cache_key)
    if response:
        result = json.loads(response)
        return result
    
    # Parse the date strings into datetime objects
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")

    # Query distinct dates from the database
    distinct_dates_query = select(Product.name).distinct()
    response = await postgres_db.fetch_all(distinct_dates_query)

    #set the cache
    serialized_data = json.dumps(response, default=str)
    redis_db.set(cache_key, serialized_data)

    return response
