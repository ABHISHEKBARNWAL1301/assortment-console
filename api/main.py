import uvicorn
from app.db import postgres_db, init_postgres_db
from app.startup import *
from app.app import app
from app.routes import abc
from app.config import settings


@app.get("/")
async def home():
    return {"Welcome": "To Assortment Planning"}


@app.on_event("startup")
async def startup():
    await init_postgres_db()
    await postgres_db.connect()
    # await load_products()



app.include_router(abc)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
