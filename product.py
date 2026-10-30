"""Product module for MiniMart inventory system."""
import re
class Product:
    """Represents a single product item in the store."""
    _total_count: int = 0  
    def __init__(self, name: str, sku: str, price: float, quantity: int):
        """Initialize a Product instance."""
        if not Product.is_valid_sku(sku):
            raise ValueError(f"Invalid SKU format: '{sku}'. Must be 3 letters followed by 3 digits.")
        self.name = name
        self.sku = sku
        self.price = price        
        self.quantity = quantity  # Invokes quantity.setter validation
        Product._total_count += 1
    @property
    def price(self) -> float:
        """Get the unit price of the product."""
        return self._price
    @price.setter
    def price(self, value: float) -> None:
        """Set the unit price with type and range validation."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Price must be a number (int or float).")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(value)
    @property
    def quantity(self) -> int:
        """Get the current stock quantity."""
        return self._quantity
    @quantity.setter
    def quantity(self, value: int) -> None:
        """Set the stock quantity with type and non-negative integer validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Quantity must be an integer.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
    @property
    def line_value(self) -> float:
        """Compute the total line value for this product (price * quantity)."""
        return self.price * self.quantity
    @property
    def is_low_stock(self) -> bool:
        """Check if stock is running low (quantity strictly below 5)."""
        return self.quantity < 5
    @classmethod
    def count(cls) -> int:
        """Return total number of Product objects created."""
        return cls._total_count
    @classmethod
    def from_csv_line(cls, line: str) -> "Product":
        """Factory method: create a Product instance from a comma-separated string line."""
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 4:
            raise ValueError("CSV line must contain exactly 4 fields: name, sku, price, quantity.")
        
        name, sku, price_str, quantity_str = parts
        price = float(price_str)
        quantity = int(quantity_str)
        return cls(name, sku, price, quantity)
    @staticmethod
    def is_valid_sku(sku: str) -> bool:
        """Validate SKU format: exactly 3 letters followed by 3 digits (e.g., 'MLK001')."""
        if not isinstance(sku, str):
            return False
        return bool(re.fullmatch(r"^[A-Za-z]{3}\d{3}$", sku))
    def __repr__(self) -> str:
        """Return clean string representation of Product."""
        return f"Product('{self.name}', '{self.sku}', {self.price}, {self.quantity})"
