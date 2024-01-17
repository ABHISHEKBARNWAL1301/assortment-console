from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    """
    Example model representing a product.
    
    Attributes:
        id (int): Primary key for the product.
        name (str): Name of the product.
        price (int): Price of the product.
        date_of_mfac (datetime): Manufacturing date of the product.
    """
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    price = Column(Integer, nullable=True)
    date_of_mfac = Column(DateTime, nullable=True)

