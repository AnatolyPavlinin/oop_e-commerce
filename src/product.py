from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def info(self) -> str:
        pass

    def __str__(self) -> str:
        pass


class CreationLogMixin:
    """Миксин для регистрации создания объекта."""

    def __init__(self, *args, **kwargs):
        # Определяем имя класса
        class_name = self.__class__.__name__
        # Объединяем аргументы в единую строку
        args_repr = ", ".join(repr(a) for a in args)
        kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        # Формируем сообщение
        message = f"Объект класса {class_name} создан с аргументами: {args_repr}, {kwargs_repr}".strip(", ")
        # Выводим сообщение
        print(message)
        # Продолжаем вызов родительского конструктора
        super().__init__(*args, **kwargs)


class Product(BaseProduct):
    """Класс товаров"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def __add__(self, other):
        """Перегрузка оператора '+', теперь складываются только товары одного класса."""
        if type(self) != type(other):
            raise TypeError("Нельзя суммировать объекты разных классов")
        return self.full_cost() + other.full_cost()

    def __str__(self) -> str:
        return f"{self.name}, {self.price:.2f} руб. Остаток: {self.quantity} шт."

    def full_cost(self) -> float:
        """Возвращает полную стоимость товара"""
        return self.price * self.quantity

    def info(self) -> str:
        """Базовая информация о товаре"""
        return f"{self.__str__()} | Описание: {self.description}"

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

    def info(self) -> str:
        """Дополнительная информация о смартфоне"""
        return (
            f"{super().__str__()} | Эффективность: {self.efficiency}, Модель: {self.model}, "
            f"Память: {self.memory} ГБ, Цвет: {self.color}"
        )


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

    def info(self) -> str:
        """Дополнительная информация о газонной траве"""
        return (
            f"{super().__str__()} | Страна: {self.country}, Герминация: {self.germination_period}, Цвет: {self.color}"
        )
