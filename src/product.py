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

    def __str__(self):
        """Добавляем строкове отображение в виде:
        Название продукта, 80 руб. Остаток: 15 шт
        """
        return f"{self.name}, {self.__price:.2f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Перегрузка оператора '+', теперь складываются только товары одного класса."""
        if type(self) != type(other):
            raise TypeError("Нельзя суммировать объекты разных классов")
        return self.full_cost() + other.full_cost()

    def full_cost(self) -> float:
        """Возвращает полную стоимость товара"""
        return self.price * self.quantity

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


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):  # Переопределяем метод __str__

        base_string = super().__str__()

        # Добавляем уникальные атрибуты смартфона
        additional_details = (
            f"\nЭффективность: {self.efficiency}%\nМодель: {self.model}\nПамять: {self.memory} ГБ\nЦвет: {self.color}"
        )
        return base_string + additional_details


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Форматирует строку для газонной травы с добавлением дополнительных атрибутов"""
        base_string = super().__str__()  # Вызываем родительский метод __str__
        additional_details = (
            f"\nСтрана: {self.country}\n" f"Герминация: {self.germination_period}\n" f"Цвет: {self.color}"
        )

        return base_string + additional_details
