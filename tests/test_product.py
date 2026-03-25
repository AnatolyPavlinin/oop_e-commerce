import contextlib
import io

import pytest

from src.product import LawnGrass, Product


def test_product_init():
    product = Product("Наушники", "Беспроводные", 4999.99, 15)

    assert product.name == "Наушники"
    assert product.description == "Беспроводные"
    assert product.price == 4999.99
    assert product.quantity == 15


# Тестируем создание нового товара
def test_new_product():
    data = {"name": "Новинка", "description": "Описание новинки", "price": "1000.50", "quantity": "5"}
    product = Product.new_product(data, [])

    # Проверяем, что атрибуты установлены верно
    assert product.name == "Новинка"
    assert product.description == "Описание новинки"
    assert product.price == 1000.50
    assert product.quantity == 5


# Тестируем новый продукт с обработкой конфликтов (уже существующий товар)
def test_new_product_conflict():
    existing_products = [
        Product("Телефончик", "Самый крутой телефон", 5000.0, 10),
        Product("Ноутбучик", "Лучший ноут", 10000.0, 5),
    ]

    # Данные для нового товара с тем же названием, что и существующий
    data = {"name": "Телефончик", "description": "Обновленное описание телефона", "price": "6000.00", "quantity": "15"}

    updated_product = Product.new_product(data, existing_products)

    # Проверяем, что существующий товар обновлён корректно
    assert updated_product.name == "Телефончик"
    assert updated_product.description == "Обновленное описание телефона"
    assert updated_product.price == 6000.0  # Новая цена выше старой
    assert updated_product.quantity == 25  # Сумма количеств (10+15)

    # Проверяем, что остальные товары остались неизменёнными
    other_product = next(p for p in existing_products if p.name == "Ноутбучик")
    assert other_product.price == 10000.0
    assert other_product.quantity == 5


# Тестируем геттер и сеттер цены
def test_price_property():
    product = Product("Книга", "Научпоп книга", 100.0, 10)

    # Проверяем получение текущей цены
    assert product.price == 100.0

    # Проверяем установку новой корректной цены
    product.price = 150.0
    assert product.price == 150.0

    # Проверяем защиту от некорректных значений
    product.price = -50.0
    assert product.price == 150.0  # Значение не изменится


def test_add_method_correctness(smartphones):
    """Проверяет правильность сложения товаров одного класса"""
    s1, s2 = smartphones[:2]
    expected_result = s1.full_cost() + s2.full_cost()
    assert s1 + s2 == expected_result


def test_add_multiple_same_class(lawngrases):
    """Проверяет сложение нескольких товаров одного класса"""
    l1, l2 = lawngrases[:2]
    third_lawn = LawnGrass(
        "Газонная трава 'Оптима'", "Оптимальная смесь", 1800, 8, "Германия", "1 неделя", "Светло-зеленый"
    )
    products = [l1, l2, third_lawn]

    # Корректно рассчитываем ожидаемое значение суммы
    expected_result = sum(p.full_cost() for p in products)
    actual_result = sum([l1.full_cost(), l2.full_cost(), third_lawn.full_cost()])
    assert actual_result == expected_result


def test_type_error_on_different_classes(smartphones, lawngrases):
    """Проверяет возникновение ошибки при попытке сложения разнородных классов"""
    s1 = smartphones[0]
    l1 = lawngrases[0]
    with pytest.raises(TypeError):
        s1 + l1


def test_add_with_base_product_and_subclass(smartphones):
    """Проверяет невозможность сложения базовых и специализированных классов"""
    p1 = Product("Базовый товар", "Описание", 1000, 5)
    s1 = smartphones[0]
    with pytest.raises(TypeError):
        p1 + s1


def test_str(sample_products):
    """Проверяет метод __str__"""
    product = sample_products[0]
    expected_output = f"{product.name}, {product.price:.2f} руб. Остаток: {product.quantity} шт."
    assert str(product) == expected_output


def test_smartphone_initialization(smartphones):
    """Проверяет правильность инициализации объекта Smartphone"""
    phone = smartphones[0]
    assert phone.name == "iPhone 14 Pro"
    assert phone.description == "Apple iPhone 14 Pro"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.efficiency == 97.5
    assert phone.model == "A16 Bionic"
    assert phone.memory == 512
    assert phone.color == "Space Black"


def test_smartphone_info_representation(smartphones):
    """Проверяет корректность метода info для смартфона"""
    phone = smartphones[0]
    expected_output = (
        f"{phone.name}, {phone.price:.2f} руб. Остаток: {phone.quantity} шт. | "
        f"Эффективность: {phone.efficiency}, Модель: {phone.model}, "
        f"Память: {phone.memory} ГБ, Цвет: {phone.color}"
    )
    assert phone.info() == expected_output


def test_smartphone_full_cost(smartphones):
    """Проверяет корректность расчёта полной стоимости смартфона"""
    phone = smartphones[0]
    expected_cost = phone.price * phone.quantity
    assert phone.full_cost() == expected_cost


def test_lawngrass_initialization(lawngrases):
    """Проверяет правильность инициализации объекта LawnGrass"""
    grass = lawngrases[0]
    assert grass.name == "Газонная трава 'Экстра'"
    assert grass.description == "Высокоэффективная смесь"
    assert grass.price == 1500
    assert grass.quantity == 10
    assert grass.country == "Россия"
    assert grass.germination_period == "2-3 недели"
    assert grass.color == "Зелёный"


def test_lawngrass_info_representation(lawngrases):
    """Проверяет корректность метода info для газонной травы"""
    grass = lawngrases[0]
    expected_output = (
        f"{grass.name}, {grass.price:.2f} руб. Остаток: {grass.quantity} шт. | "
        f"Страна: {grass.country}, Герминация: {grass.germination_period}, Цвет: {grass.color}"
    )
    assert grass.info() == expected_output


def test_lawngrass_full_cost(lawngrases):
    """Проверяет корректность расчёта полной стоимости газонной травы"""
    grass = lawngrases[0]
    expected_cost = grass.price * grass.quantity
    assert grass.full_cost() == expected_cost


def test_base_product_str_representation(sample_products):
    """Проверяет корректность метода __str__ для класса BaseProduct с несколькими объектами"""
    expected_outputs = ["Телефон, 19999.99 руб. Остаток: 10 шт.", "Ноутбук, 79999.50 руб. Остаток: 5 шт."]

    for idx, product in enumerate(sample_products):
        assert str(product) == expected_outputs[idx], f"Ошибка при проверке объекта {idx + 1}"


def test_base_product_init_attributes(sample_products):
    """Проверяет установку атрибутов через инициализатор абстрактного класса"""
    first_product = sample_products[0]  # Берём первый продукт из списка
    second_product = sample_products[1]  # Берём второй продукт из списка

    # Проверяем атрибуты первого продукта
    assert first_product.name == "Телефон"
    assert first_product.description == "Смартфон"
    assert first_product.price == 19999.99
    assert first_product.quantity == 10

    # Проверяем атрибуты второго продукта
    assert second_product.name == "Ноутбук"
    assert second_product.description == "Игровой ноутбук"
    assert second_product.price == 79999.50
    assert second_product.quantity == 5


def test_creation_log_mixin(loggable_product):
    """Проверяет корректность работы миксина CreationLogMixin"""
    # Готовим буфер для вывода
    buffer = io.StringIO()

    # Перенаправляем вывод в буфер
    with contextlib.redirect_stdout(buffer):
        # Создаем объект с фиксированными параметрами
        loggable_product("Тестовый продукт", "Тестовое описание", 123.45, 10)

    # Получаем содержание буфера
    output = buffer.getvalue().strip()

    # Ожидаемое сообщение
    expected_message = (
        "Объект класса LoggedProduct создан с аргументами: 'Тестовый продукт', 'Тестовое описание', 123.45, 10"
    )

    assert output == expected_message


def test_zero_quantity_raises_error():
    """
    Тест проверяет, что создание товара с quantity=0
    вызывает исключение ValueError с правильным сообщением.
    """

    with pytest.raises(ValueError) as exc_info:
        Product("Бананы", "Вкусные", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
