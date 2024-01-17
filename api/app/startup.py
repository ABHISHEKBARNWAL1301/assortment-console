import pandas as pd, os, numpy as np
from sqlalchemy import insert, text, cast, Date
from .config import settings
from .db import  postgres_db
from app.models import *
 


csv_folder = os.path.join(os.getcwd(),"../corpus_files")


#loading data to db
async def insert_into_db(model, file_name, batch_size=1000):
    try:
        truncate_statement = text(f"TRUNCATE TABLE {model.__tablename__}")
        await postgres_db.execute(truncate_statement)
    except Exception as e:
        print(e)
        raise e
    try:
        # Load the CSV file into a DataFrame
        csv_file_path = os.path.join(csv_folder, file_name)
        for chunk in pd.read_csv(csv_file_path, chunksize=batch_size):
            # Handle data-specific conversions
            # if file_name == "product.csv" and 'date' in chunk:
            #     chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')  
            # Filter out rows with NaN values
            # chunk = chunk.dropna()
            chunk = chunk.replace({np.nan: None})   
            # Remove duplicate rows
            chunk = chunk.drop_duplicates()
            # Insert the current batch into the database
            await postgres_db.execute(insert(model).values(chunk.to_dict(orient="records")))
        
        print(f"{model.__tablename__} loaded successfully")
    except Exception as e:
        print(e)
        raise e


async def load_products():
    print("Loading probability")
    await insert_into_db(Product, "product.csv")







 