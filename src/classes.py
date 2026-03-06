from typing import List

class Product:
    """Класс товаров"""
    name: str # название
    description: str # описание
    price: int
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int)-> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категорий"""
    name: str # название
    description: str # описание
    products: list # список товаров

    # атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product])-> None:
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.products = products

        # обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)
