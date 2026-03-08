from src.category import Category
from src.product import Product


def test_category_init(sample_products, reset_category_counters):
    category = Category("Электроника", "Техника и гаджеты", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"
    expected_product_strings = "\n".join(
        [f"{p.name}, {p.price:.2f} руб. Остаток: {p.quantity} шт." for p in sample_products]
    )
    actual_product_strings = category.products
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


# Тестируем геттер getting_list_of_product
def test_getting_list_of_product(sample_products, reset_category_counters):
    category = Category("Электроника", "Раздел электронной техники", sample_products)

    # Проверяем корректность формата вывода списка товаров
    expected_output = "Телефон, 19999.99 руб. Остаток: 10 шт.\n" "Ноутбук, 79999.50 руб. Остаток: 5 шт."
    assert category.products == expected_output
