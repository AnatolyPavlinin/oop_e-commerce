import json
import os
from typing import List

from src.category import Category, Product


def load_categories_from_json(json_file: str) -> List[Category]:
    """Функция читает данные из json-файла и возваращает список категорий товаров"""
    full_path = os.path.abspath("../data/products.json")
    with open(full_path, "r", encoding="UTF-8") as file:
        categories_data = json.load(file)
    categories = []
    for cat_data in categories_data:
        products_list = [
            Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
            for prod in cat_data["products"]
        ]
        category = Category(cat_data["name"], cat_data["description"], products_list)
        categories.append(category)

    return categories


# if __name__ == "__main__":
#     categories = load_categories_from_json('categories.json')
#
#     for category in categories:
#         print(f"\n== Категория: {category.name} ==\nОписание: {category.description}\n")
#         for product in category.products:
#             print(product)
