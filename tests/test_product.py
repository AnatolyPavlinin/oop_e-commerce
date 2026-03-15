import pytest

from src.product import LawnGrass, Product, Smartphone


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


def test_empty_product_case(smartphones):
    """Проверяет случай с нулевым количеством товара"""
    s1 = smartphones[0]
    empty_product = Smartphone("Empty Phone", "No Description", 0, 0, 0, "Model X", 0, "Black")
    result = s1 + empty_product
    assert result == s1.full_cost()


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


def test_smartphone_str_representation(smartphones):
    """Проверяет корректность метода __str__ для смартфона"""
    phone = smartphones[0]
    expected_output = (
        f"{phone.name}, {phone.price:.2f} руб. Остаток: {phone.quantity} шт.\n"
        f"Эффективность: {phone.efficiency}%\n"
        f"Модель: {phone.model}\n"
        f"Память: {phone.memory} ГБ\n"
        f"Цвет: {phone.color}"
    )
    assert str(phone) == expected_output


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


def test_lawngrass_str_representation(lawngrases):
    """Проверяет корректность метода __str__ для газонной травы"""
    grass = lawngrases[0]
    expected_output = (
        f"{grass.name}, {grass.price:.2f} руб. Остаток: {grass.quantity} шт.\n"
        f"Страна: {grass.country}\n"
        f"Герминация: {grass.germination_period}\n"
        f"Цвет: {grass.color}"
    )
    assert str(grass) == expected_output


def test_lawngrass_full_cost(lawngrases):
    """Проверяет корректность расчёта полной стоимости газонной травы"""
    grass = lawngrases[0]
    expected_cost = grass.price * grass.quantity
    assert grass.full_cost() == expected_cost
