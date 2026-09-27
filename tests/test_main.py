from src.main import Category


def test_init_product(product):
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 10.7
    assert product.quantity == 100


def test_init_category(category):
    assert category.name == "Test Category"
    assert category.description == "Test description"
    assert len(category.products) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3
