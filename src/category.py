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

    def __str__(self):
        """Добавляем строкове отображение в виде:
        Название категории, количество продуктов: 200 шт.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт"

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию.
        product: Объект типа Product или его подкласс
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Возникла ошибка TypeError при добавлении не продукта")

    @property
    def products(self):
        """
        Геттер, который выводит список товаров в формате:
        Продукт, 'цена' руб. Остаток: '' шт.
        """
        return "\n".join(map(str, self.__products))

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник  всех товаров в категории.
        Если товаров нет, возвращает 0.0.
        """
        try:
            # Создаем список цен всех товаров в категории
            prices = [product.price for product in self.__products]

            return sum(prices) / len(prices)

        except ZeroDivisionError:
            return 0.0
