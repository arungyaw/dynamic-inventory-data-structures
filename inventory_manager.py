import heapq
from avl_tree import AVLTree


class InventoryManager:
    def __init__(self):
        # Main hash table.
        # SKU is the key, and the Product object is the value.
        self.products = {}

        # Category index.
        # Each category points to a set of SKUs in that category.
        self.category_index = {}

        # Min-heap for restocking.
        # The product with the lowest stock priority comes out first.
        self.restock_heap = []

        # AVL tree for price-based searching.
        # This lets us search products by price range.
        self.price_tree = AVLTree()

    def _restock_priority(self, product):
        # This method calculates how urgently a product needs restocking.
        # Lower priority value means the product needs restocking sooner.

        # If reorder_level is 0 or less, avoid division by zero.
        if product.reorder_level <= 0:
            return float("inf")

        # Example: quantity 2 and reorder level 5 gives 0.4,
        # which means it is below the reorder level and should be restocked.
        return product.quantity / product.reorder_level

    def add_product(self, product):
        # Do not allow duplicate SKUs because SKU should be unique.
        if product.sku in self.products:
            raise ValueError("Product with this SKU already exists.")

        # Add the product to the main hash table.
        self.products[product.sku] = product

        # If this category does not exist yet, create an empty set for it.
        if product.category not in self.category_index:
            self.category_index[product.category] = set()

        # Add the product SKU to the correct category.
        self.category_index[product.category].add(product.sku)

        # Add the product price and SKU to the AVL tree.
        # This supports price-range searching later.
        self.price_tree.insert(product.price, product.sku)

        # Calculate restock priority and add it to the heap.
        priority = self._restock_priority(product)
        heapq.heappush(self.restock_heap, (priority, product.sku))

    def search_by_sku(self, sku):
        # Search for a product directly by SKU.
        # If the SKU does not exist, this returns None.
        return self.products.get(sku)

    def search_by_category(self, category):
        # Get all SKUs for the requested category.
        # If the category does not exist, use an empty set.
        sku_set = self.category_index.get(category, set())

        # Convert SKUs back into full Product objects.
        # Sorting keeps the output consistent during testing.
        return [self.products[sku] for sku in sorted(sku_set)]

    def search_by_price_range(self, low, high):
        # Ask the AVL tree for all SKUs with prices in the selected range.
        sku_list = self.price_tree.range_search(low, high)

        # Convert the matching SKUs into Product objects.
        return [self.products[sku] for sku in sorted(sku_list)]

    def update_quantity(self, sku, new_quantity):
        # Find the product before trying to update it.
        product = self.products.get(sku)

        # If the product does not exist, return False.
        if product is None:
            return False

        # Update the stock quantity.
        product.quantity = new_quantity

        # Add a new heap entry with the updated priority.
        # Old heap entries are handled by lazy deletion later.
        priority = self._restock_priority(product)
        heapq.heappush(self.restock_heap, (priority, sku))

        return True

    def get_next_restock_item(self):
        # Keep checking the heap until a valid restock item is found.
        while self.restock_heap:
            priority, sku = heapq.heappop(self.restock_heap)

            # Get the current product from the main hash table.
            product = self.products.get(sku)

            # If the product no longer exists, skip it.
            if product is None:
                continue

            # Recalculate current priority to check if this heap entry is old.
            current_priority = self._restock_priority(product)

            # If the heap priority does not match the current product data,
            # it means this is an old entry, so skip it.
            if priority != current_priority:
                continue

            # Return the product only if it is actually at or below reorder level.
            if product.quantity <= product.reorder_level:
                return product

        # If no product needs restocking, return None.
        return None