import pytest

from src.category import Category
from src.product import Product


def test_category_init(sample_products):
    category = Category("Электроника", "Техника и гаджеты", sample_products)

    # Проверка базовых атрибутов
    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"

    # Проверка строки категории
    expected_category_string = "Электроника, количество продуктов: 15 шт"
    assert str(category) == expected_category_string

    # Проверка содержимого товаров (используем временный доступ к приватному атрибуту)
    expected_product_strings = "\n".join(
        [f"{p.name}, {p.price:.2f} руб. Остаток: {p.quantity} шт." for p in sample_products]
    )
    actual_product_strings = "\n".join(map(str, category._Category__products))  # Доступ к приватному атрибуту
    assert actual_product_strings == expected_product_strings


def test_category_count(sample_products, reset_category_counters):
    Category("Электроника", "Техника", sample_products)
    Category("Одежда", "Мужская одежда", [])

    assert Category.category_count == 2


def test_product_count(sample_products, reset_category_counters):
    Category("Электроника", "Техника", sample_products)
    Category("Одежда", "Мужская одежда", [])

    assert Category.product_count == 2


def test_add_product(sample_products, reset_category_counters):
    category = Category("Техногаджеты", "Раздел техники и гаджетов", sample_products[:])  # Передача копий товаров
    product_to_add = Product("Планшет", "Таблетка", 15000.00, 3)
    category.add_product(product_to_add)

    # Проверяем, что продукт добавлен
    expected_output = (
        "Телефон, 19999.99 руб. Остаток: 10 шт.\n"
        "Ноутбук, 79999.50 руб. Остаток: 5 шт.\n"
        "Планшет, 15000.00 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output

    # Проверяем, что общий счетчик продуктов увеличен
    assert Category.product_count == 3


def test_valid_product_addition(sample_category, valid_products):
    """Проверяет успешное добавление валидных продуктов"""
    for product in valid_products:
        sample_category.add_product(product)
        assert product in sample_category._Category__products  # Проверяем, что продукт попал в список
        assert Category.product_count > 0  # Проверяем увеличение общего количества продуктов


def test_invalid_product_addition(sample_category, invalid_objects):
    """Проверяет обработку попыток добавления недопустимых объектов"""
    for obj in invalid_objects:
        with pytest.raises(TypeError):
            sample_category.add_product(obj)


def test_product_count_update(sample_category, valid_products):
    """Проверяет обновление количества продуктов при добавлении новых элементов"""
    initial_count = Category.product_count
    for product in valid_products:
        sample_category.add_product(product)
    final_count = Category.product_count
    assert final_count == initial_count + len(valid_products)


def test_multiple_additions(sample_category, valid_products):
    """Проверяет множественное добавление продуктов"""
    for product in valid_products:
        sample_category.add_product(product)
    assert len(sample_category._Category__products) == len(valid_products)


def test_reset_after_test(reset_category_counters):
    """Проверяет восстановление счётчика после завершения тестов"""


# Тестируем геттер getting_list_of_product
def test_getting_list_of_product(sample_products, reset_category_counters):
    category = Category("Электроника", "Раздел электронной техники", sample_products)

    # Проверяем корректность формата вывода списка товаров
    expected_output = "Телефон, 19999.99 руб. Остаток: 10 шт.\n" "Ноутбук, 79999.50 руб. Остаток: 5 шт."
    assert category.products == expected_output


def test_category_str(sample_products):
    """Тестирует метод __str__"""
    category = Category("Электроника", "Электронные устройства", sample_products)
    expected_output = "Электроника, количество продуктов: 15 шт"
    assert str(category) == expected_output


def test_average_price_for_empty_category():
    """
    Проверяет, что метод average_price возвращает 0.0,
    если в категории нет товаров.
    """
    # Создаем пустую категорию
    empty_category = Category(name="Пустая", description="нету")
    result = empty_category.middle_price()
    assert result == 0.0


def test_average_price_with_products(category_with_products):
    """
    Проверяет корректность расчета средней цены (ценника).
    """

    headphones = Product("Наушники", "Беспроводные", 5000.00, 15)
    category_with_products.add_product(headphones)
    result = category_with_products.middle_price()
    expected_average = 34999.83
    assert result == pytest.approx(expected_average)
