from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class ProductResponse(BaseModel):
    """
    Pydantic model for the response representing a product.

    Attributes:
        id (int): Primary key for the product.
        name (str): Name of the product.
        price (int): Price of the product.
        date_of_mfac (datetime): Manufacturing date of the product.
    """
    id: int
    name: str
    price: int
    date_of_mfac: datetime
