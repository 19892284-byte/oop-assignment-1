"""Bonus pytest test suite for validation rules."""

import pytest
from product import Product
def test_product_valid_creation():
    p = Product("Milk", "MLK001", 1.25, 12)
    assert p.name == "Milk"
    assert p.sku == "MLK001"
    assert p.price == 1.25
    assert p.quantity == 12
    assert p.line_value == 15.0
    assert not p.is_low_stock

def test_invalid_price_type():
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", "invalid_price", 10)

def test_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", -5.0, 10)

def test_invalid_quantity_type():
    with pytest.raises(TypeError):
        Product("Milk", "MLK001", 2.50, 3.14)

def test_negative_quantity_raises_value_error():
    with pytest.raises(ValueError):
        Product("Milk", "MLK001", 2.50, -3)

def test_invalid_sku_format():
    with pytest.raises(ValueError):
        Product("Milk", "INVALID_SKU", 2.50, 10)

def test_low_stock_property():
    p = Product("Bread", "BRD002", 0.90, 3)
    assert p.is_low_stock
