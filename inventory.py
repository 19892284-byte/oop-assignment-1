"""Inventory management module for MiniMart."""
from product import Product
class Inventory:
    """Manages a collection of Product objects indexed by their SKU."""
    def __init__(self):
        """Initialize an empty inventory dictionary."""
        self._products: dict[str, Product] = {}
    def add(self, product: Product) -> None:
        """Add a Product to the inventory using its SKU as key."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to the inventory.")
        self._products[product.sku] = product

    def remove(self, sku: str) -> Product:
        """Remove and return a Product by SKU. Raises KeyError if not found."""
        if sku not in self._products:
            raise KeyError(f"Product with SKU '{sku}' not found in inventory.")
        return self._products.pop(sku)
    def find(self, sku: str) -> Product | None:
        """Find and return a Product by SKU, or None if not found."""
        return self._products.get(sku)
    def total_value(self) -> float:
        """Calculate and return total value of all products in stock."""
        return sum(p.line_value for p in self._products.values())
    def get_low_stock_items(self) -> list[Product]:
        """Return a list of all items currently on low stock (< 5 units)."""
        return [p for p in self._products.values() if p.is_low_stock]
    def all_products(self) -> list[Product]:
        """Return a list of all products in the inventory."""
        return list(self._products.values())
    @classmethod
    def from_lines(cls, lines: list[str]) -> "Inventory":
        """Factory method: create an Inventory instance populated from a list of CSV string lines."""
        inventory = cls()
        for line in lines:
            if line.strip():  
                product = Product.from_csv_line(line)
                inventory.add(product)
        return inventory
