from product import Product
from inventory_manager import InventoryManager


def main():
    # Create one inventory manager object.
    # This object controls all the data structures.
    inventory = InventoryManager()

    # Create sample products for the proof-of-concept demo.
    products = [
        Product("SKU001", "Laptop Stand", "Electronics", 35.99, 8, 5),
        Product("SKU002", "Wireless Mouse", "Electronics", 24.99, 2, 5),
        Product("SKU003", "Notebook", "Office", 4.99, 25, 10),
        Product("SKU004", "Desk Lamp", "Office", 49.99, 3, 4),
        Product("SKU005", "USB Cable", "Electronics", 9.99, 1, 8),
    ]

    # Add each product to the inventory.
    # This updates the hash table, category index, AVL tree, and heap.
    for product in products:
        inventory.add_product(product)

    # Demonstrate SKU lookup using the hash table.
    print("Search by SKU:")
    print(inventory.search_by_sku("SKU002"))

    # Demonstrate category search using the category index.
    print("\nSearch by category: Electronics")
    for product in inventory.search_by_category("Electronics"):
        print(product)

    # Demonstrate price-range search using the AVL tree.
    print("\nSearch by price range: $10 to $40")
    for product in inventory.search_by_price_range(10, 40):
        print(product)

    # Demonstrate restock priority using the min-heap.
    print("\nNext restock item:")
    print(inventory.get_next_restock_item())

    # Update one product quantity to show that priority changes.
    print("\nUpdate quantity for SKU001 to 1")
    inventory.update_quantity("SKU001", 1)

    # Show the next restock item after the update.
    print("Next restock item after update:")
    print(inventory.get_next_restock_item())


if __name__ == "__main__":
    main()