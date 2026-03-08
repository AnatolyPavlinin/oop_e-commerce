from src.product import Product


class Category:
    """Класс категорий"""

    name: str  # название
    description: str  # описание
    products: list  # приватный список товаров

    # атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, initial_products=None) -> None:
        """Метод, который инициализирует экземпляры класса.
        name: Название категории
        description: Описание категории
        initial_products: Список начальных продуктов (если пустой - создаётся пустой список)
        """

        if initial_products is None:
            initial_products = []

        self.name = name
        self.description = description
        self.__products = initial_products

        # обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(initial_products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.
        product: Объект типа Product
        """
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем общее число продуктов

    @property
    def products(self):
        """
        Геттер, который выводит список товаров в формате:
        Продукт, 'цена' руб. Остаток: '' шт.
        """
        result = []  # Используем список для хранения каждой записи
        for product in self.__products:
            result.append(f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)  # Объединяем элементы списка с переносом строки
