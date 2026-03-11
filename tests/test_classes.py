from src.classes import Category, Product


def test_product_init():
    product = Product("Наушники", "Беспроводные", 4999.99, 15)

    assert product.name == "Наушники"
    assert product.description == "Беспроводные"
    assert product.price == 4999.99
    assert product.quantity == 15


def test_category_init(sample_products, reset_category_counters):
    category = Category("Электроника", "Техника и гаджеты", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"
    assert category.products == sample_products


def test_category_count(sample_products, reset_category_counters):
    Category("Электроника", "Техника", sample_products)
    Category("Одежда", "Мужская одежда", [])

    assert Category.category_count == 2


def test_product_count(sample_products, reset_category_counters):
    Category("Электроника", "Техника", sample_products)
    Category("Одежда", "Мужская одежда", [])

    assert Category.product_count == 2
