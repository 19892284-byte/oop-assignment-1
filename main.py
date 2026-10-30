"""Demonstration script for MiniMart store inventory system."""
from inventory import Inventory
SAMPLE_DATA = [
    "Milk, MLK001,1.25,12",
    "Bread, BRD002,0.90,3",
    "Eggs, EGG003,2.40,30",
    "Coffee, COF004,7.50,2",
]
def main():
    """Build inventory from sample data and output a neatly formatted report."""
    inventory = Inventory.from_lines(SAMPLE_DATA)
    print("=" * 60)
    print(f"{'MiniMart Inventory Report':^60}")
    print("=" * 60)
    print(f"{'Name':<12} | {'SKU':<8} | {'Price':<8} | {'Qty':<5} | {'Line Value':<10}")
    print("-" * 60)

    for item in inventory.all_products():
        print(
            f"{item.name:<12} | {item.sku:<8} | ${item.price:<7.2f} | "
            f"{item.quantity:<5} | ${item.line_value:<9.2f}"
        )

    print("-" * 60)
    print(f"Total Inventory Value: ${inventory.total_value():.2f}")
    print("=" * 60)

    print("\n[Low Stock Alert (Quantity < 5)]")
    low_stock_list = inventory.get_low_stock_items()
    if low_stock_list:
        for item in low_stock_list:
            print(f" -> {item.name} (SKU: {item.sku}) - Only {item.quantity} units left!")
    else:
        print(" -> All products are well stocked.")
    print("=" * 60)

if __name__ == "__main__":
    main()
