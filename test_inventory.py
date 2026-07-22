from product import Product
from inventory_manager import InventoryManager


def run_tests():
    # This list stores readable test results.
    # The results will be printed and also saved to a text file.
    results = []

    # Create the inventory manager for testing.
    inventory = InventoryManager()

    # Create sample products for the test cases.
    products = [
        Product("SKU001", "Laptop Stand", "Electronics", 35.99, 8, 5),
        Product("SKU002", "Wireless Mouse", "Electronics", 24.99, 2, 5),
        Product("SKU003", "Notebook", "Office", 4.99, 25, 10),
        Product("SKU004", "Desk Lamp", "Office", 49.99, 3, 4),
        Product("SKU005", "USB Cable", "Electronics", 9.99, 1, 8),
    ]

    # Add all sample products to the inventory.
    for product in products:
        inventory.add_product(product)

    # Test 1: Search for an existing SKU.
    assert inventory.search_by_sku("SKU002").name == "Wireless Mouse"
    results.append("Test 1 Passed: Search by existing SKU returned Wireless Mouse.")

    # Test 2: Search for a SKU that does not exist.
    assert inventory.search_by_sku("SKU999") is None
    results.append("Test 2 Passed: Search by missing SKU returned None.")

    # Test 3: Search by category.
    electronics = inventory.search_by_category("Electronics")
    assert len(electronics) == 3
    results.append("Test 3 Passed: Category search returned 3 Electronics products.")

    # Test 4: Search products in a price range.
    price_results = inventory.search_by_price_range(10, 40)
    price_names = [product.name for product in price_results]

    assert "Wireless Mouse" in price_names
    assert "Laptop Stand" in price_names
    results.append("Test 4 Passed: Price range search returned correct products.")

    # Test 5: Check the first restock item.
    # USB Cable has the lowest stock ratio, so it should appear first.
    restock_item = inventory.get_next_restock_item()
    assert restock_item.sku == "SKU005"
    results.append("Test 5 Passed: Restock priority returned USB Cable first.")

    # Test 6: Update product quantity and check whether heap priority changes.
    inventory.update_quantity("SKU001", 1)
    updated_item = inventory.get_next_restock_item()

    assert updated_item.sku == "SKU001"
    results.append("Test 6 Passed: Quantity update changed restock priority correctly.")

    # Save the test results into a text file for the report.
    with open("phase2_test_results.txt", "w") as file:
        for result in results:
            file.write(result + "\n")

    # Print results in the terminal so we can take a screenshot.
    for result in results:
        print(result)


if __name__ == "__main__":
    run_tests()