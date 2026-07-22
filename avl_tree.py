class AVLNode:
    def __init__(self, price, sku):
        # Each AVL node stores a price as the main key.
        # A set of SKUs is used because more than one product can have the same price.
        self.price = price
        self.skus = {sku}

        # Left and right child nodes are used like a normal binary search tree.
        self.left = None
        self.right = None

        # Height is needed to check whether the AVL tree is balanced.
        self.height = 1


class AVLTree:
    def __init__(self):
        # The root is the first node in the tree.
        # It starts as None because the tree is empty at the beginning.
        self.root = None

    def get_height(self, node):
        # If the node does not exist, its height is 0.
        if node is None:
            return 0

        # Otherwise, return the height stored in the node.
        return node.height

    def get_balance(self, node):
        # Balance factor tells whether the tree is left-heavy or right-heavy.
        if node is None:
            return 0

        # Positive value means left side is taller.
        # Negative value means right side is taller.
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        # Right rotation is used when the left side of the tree becomes too heavy.
        x = y.left
        temp = x.right

        # Move x above y.
        x.right = y
        y.left = temp

        # Update heights after rotation.
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        # Return the new root after rotation.
        return x

    def rotate_left(self, x):
        # Left rotation is used when the right side of the tree becomes too heavy.
        y = x.right
        temp = y.left

        # Move y above x.
        y.left = x
        x.right = temp

        # Update heights after rotation.
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root after rotation.
        return y

    def insert(self, price, sku):
        # Public insert method.
        # It updates the root because rotations can change the root node.
        self.root = self._insert(self.root, price, sku)

    def _insert(self, node, price, sku):
        # If the current spot is empty, create a new node.
        if node is None:
            return AVLNode(price, sku)

        # If the new price is smaller, insert it on the left side.
        if price < node.price:
            node.left = self._insert(node.left, price, sku)

        # If the new price is larger, insert it on the right side.
        elif price > node.price:
            node.right = self._insert(node.right, price, sku)

        else:
            # If the price already exists, add the SKU to the same price node.
            node.skus.add(sku)
            return node

        # Update the height of the current node after insertion.
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Check if the current node became unbalanced.
        balance = self.get_balance(node)

        # Case 1: Left Left case.
        if balance > 1 and price < node.left.price:
            return self.rotate_right(node)

        # Case 2: Right Right case.
        if balance < -1 and price > node.right.price:
            return self.rotate_left(node)

        # Case 3: Left Right case.
        if balance > 1 and price > node.left.price:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Case 4: Right Left case.
        if balance < -1 and price < node.right.price:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        # If the node is already balanced, return it normally.
        return node

    def range_search(self, low, high):
        # Public method for finding all SKUs within a price range.
        result = []
        self._range_search(self.root, low, high, result)
        return result

    def _range_search(self, node, low, high, result):
        # Stop if there is no node to search.
        if node is None:
            return

        # If the current price is greater than the low value,
        # there may be valid prices on the left side.
        if node.price > low:
            self._range_search(node.left, low, high, result)

        # If the current price is inside the range,
        # add all SKUs stored at this price.
        if low <= node.price <= high:
            result.extend(node.skus)

        # If the current price is less than the high value,
        # there may be valid prices on the right side.
        if node.price < high:
            self._range_search(node.right, low, high, result)