import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон", 19999.99, 10),
        Product("Ноутбук", "Игровой ноутбук", 79999.50, 5),
    ]


@pytest.fixture
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
