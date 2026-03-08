class Product:
    """Класс товаров"""

    name: str  # название
    description: str  # описание
    price: int  # цена
    quantity: int  # количество

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None) -> "Product":
        """
        Класc-метод, принимающий словарь с параметрами товара и список имеющихся товаров.
        Если такой товар уже существует (совпадает название), обновление количества и цены.
        Иначе создает новый объект Product.
        """
        # По умолчанию используем пустой список, если существующих товаров нет
        if existing_products is None:
            existing_products = []

        # Поиск существующего товара по названию
        found_product = next((item for item in existing_products if item.name == data["name"]), None)

        if found_product:
            # Обновляем количество и выбираем наибольшую цену
            found_product.quantity += int(data["quantity"])
            found_product.price = max(found_product.price, float(data["price"]))
            found_product.description = data["description"]
            return found_product
        else:
            # Если товар не найден, создаем новый объект
            return cls(
                name=data["name"],
                description=data["description"],
                price=float(data["price"]),
                quantity=int(data["quantity"]),
            )

    @property
    def price(self) -> float:
        """Геттер для получения текущего значения цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для установки новой цены с проверкой на недопустимое значение"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")  # Сообщение в консоль
        else:
            self.__price = value  # Устанавливаем новое значение, если оно валидно
