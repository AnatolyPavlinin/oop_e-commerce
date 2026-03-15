import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphones():
    return [
        Smartphone("iPhone 14 Pro", "Apple iPhone 14 Pro", 120000, 5, 97.5, "A16 Bionic", 512, "Space Black"),
        Smartphone("Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra", 110000, 3, 95.5, "Exynos 2300", 256, "White"),
    ]


@pytest.fixture
def lawngrases():
    return [
        LawnGrass("Газонная трава 'Экстра'", "Высокоэффективная смесь", 1500, 10, "Россия", "2-3 недели", "Зелёный"),
        LawnGrass(
            "Газонная трава 'Люкс'", "Элитная газонная трава", 2000, 5, "Голландия", "1-2 недели", "Темно-зелёный"
        ),
    ]


@pytest.fixture
def sample_category():
    """Создаёт образец категории для тестов"""
    return Category(name="Электроника", description="Каталог электроники")


@pytest.fixture
def valid_products():
    """Создание набора валидных продуктов"""
    return [
        Product("Телефон", "Смартфон", 19999.99, 10),
        Smartphone("iPhone 14 Pro", "Apple iPhone 14 Pro", 120000, 5, 97.5, "A16 Bionic", 512, "Space Black"),
        LawnGrass("Газонная трава 'Экстра'", "Высокоэффективная смесь", 1500, 10, "Россия", "2-3 недели", "Зелёный"),
    ]


@pytest.fixture
def invalid_objects():
    """Создание набора недопустимых объектов"""
    return ["String", 123, True, {"key": "value"}]
