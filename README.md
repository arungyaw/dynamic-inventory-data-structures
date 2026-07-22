# Dynamic Inventory Data Structures

## Purpose

This project is a Phase 2 proof-of-concept implementation for a dynamic inventory management system. It demonstrates how different data structures can support common inventory operations such as product lookup, category filtering, price-range searching, quantity updates, and restocking priority.

## Data Structures Used

* Hash table using a Python dictionary for SKU-based product lookup.
* Dictionary of sets for category indexing.
* Min-heap priority queue for restocking priority.
* Partial AVL tree for price-range searching.

## Files

* `product.py`: Defines the Product class and stores product information.
* `avl_tree.py`: Implements AVL insertion and price-range search.
* `inventory_manager.py`: Connects the hash table, category index, heap, and AVL tree.
* `demo.py`: Demonstrates the main inventory operations with sample products.
* `test_inventory.py`: Runs test cases and creates the test results file.
* `phase2_test_results.txt`: Stores the test results after running `test_inventory.py`.

## How to Run the Project

First, run the demonstration file:

```bash
python demo.py
```

This shows the main operations of the proof-of-concept system, including:

* Searching by SKU
* Searching by category
* Searching by price range
* Getting the next restock item
* Updating quantity and checking restock priority again

Next, run the test file:

```bash
python test_inventory.py
```

This runs the test cases and creates a file named:

```bash
phase2_test_results.txt
```

## Expected Test Results

After running `test_inventory.py`, the terminal should show six passed test cases:

```text
Test 1 Passed: Search by existing SKU returned Wireless Mouse.
Test 2 Passed: Search by missing SKU returned None.
Test 3 Passed: Category search returned 3 Electronics products.
Test 4 Passed: Price range search returned correct products.
Test 5 Passed: Restock priority returned USB Cable first.
Test 6 Passed: Quantity update changed restock priority correctly.
```

The same results should also be saved in `phase2_test_results.txt`.

## Recommended Run Order

Run the files in this order:

```bash
python demo.py
python test_inventory.py
```

Use the terminal output from these commands as evidence for the Phase 2 report.

## Summary

The proof-of-concept shows that the inventory system can add products, search by SKU, filter by category, search by price range, update product quantity, and identify restocking priority. The implementation is not the final full application yet, but it demonstrates the key data structures needed for the complete inventory management system.
