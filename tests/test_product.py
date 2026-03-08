from src.product import Product


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
