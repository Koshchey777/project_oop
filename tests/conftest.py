import pytest

from src.class_lawngrass import LawnGrass
from src.class_smartphone import Smartphone
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
def product_():
    return Product("Test Product", "Test description", 10.7, 100)


@pytest.fixture
def category():
    p1 = Product("Apple", "Red fruit", 10.0, 5)
    p2 = Product("Orange", "Citrus fruit", 15.0, 3)
    p3 = Product("Pear", "Sweet fruit", 12.0, 4)
    return Category("Test Category", "Test description", [p1, p2, p3])


@pytest.fixture
def example_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def example_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
