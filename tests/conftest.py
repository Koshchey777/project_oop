import pytest

from src.main import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счётчики класса перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product():
    return Product("Test Product", "Test description", 10.7, 100)


@pytest.fixture
def category():
    p1 = Product("Apple", "Red fruit", 10.0, 5)
    p2 = Product("Orange", "Citrus fruit", 15.0, 3)
    p3 = Product("Pear", "Sweet fruit", 12.0, 4)
    return Category("Test Category", "Test description", [p1, p2, p3])


@pytest.fixture
def category_():
    p1 = Product("Apple", "Red fruit", 10.0, 5)
    p2 = Product("Orange", "Citrus fruit", 15.0, 3)
    p3 = Product("Pear", "Sweet fruit", 12.0, 4)
    return Category("Test Category", "Test description", [p1, p2, p3])
