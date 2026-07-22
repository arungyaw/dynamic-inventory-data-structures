from dataclasses import dataclass


@dataclass
class Product:
    # This class stores the basic information for each product in the inventory.
    # I am using a dataclass here because it keeps the code simple and readable.

    sku: str            # Unique product ID used for fast lookup
    name: str           # Product name
    category: str       # Product category, such as Electronics or Office
    price: float        # Product price
    quantity: int       # Current stock quantity
    reorder_level: int  # Minimum quantity before the item should be restocked