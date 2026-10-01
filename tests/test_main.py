import pytest

from src.main import Category, IterProducts, Product


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


def test_category_count_multiple():
    """Счётчики накапливаются при создании нескольких категорий."""
    p1 = Product("Apple", "Red", 10.0, 5)
    c1 = Category("Cat1", "Desc1", [p1])
    c2 = Category("Cat2", "Desc2", [p1, p1])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_new_product_creates_new():
    goods = []
    data = {"name": "Apple", "description": "Red fruit", "price": 10.0, "quantity": 5}
    result = Product.new_product(data, goods)

    assert isinstance(result, Product)
    assert result.name == "Apple"
    assert result.price == 10.0
    assert result.quantity == 5
    assert len(goods) == 0  # список не изменился


def test_new_product_updates_existing():
    p1 = Product("Apple", "Red fruit", 10.0, 5)
    goods = [p1]
    data = {"name": "Apple", "description": "Red fruit", "price": 12.0, "quantity": 3}
    result = Product.new_product(data, goods)

    assert result is p1  # возвращён тот же объект
    assert result.quantity == 8  # 5 + 3
    assert result.price == 12.0  # max(10, 12)


def test_new_product_updates_existing_lower_price():
    p1 = Product("Apple", "Red fruit", 15.0, 5)
    goods = [p1]
    data = {"name": "Apple", "description": "Red fruit", "price": 10.0, "quantity": 2}
    result = Product.new_product(data, goods)

    assert result.price == 15.0  # max(15, 10)
    assert result.quantity == 7


def test_price_getter(product):
    assert product.price == 10.7


def test_price_setter_higher(product):
    product.price = 20.0
    assert product.price == 20.0


def test_price_setter_zero(product, capsys):
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 10.7  # цена не изменилась


def test_price_setter_negative(product, capsys):
    product.price = -5.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 10.7


def test_price_setter_lower_with_yes(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 5.0
    assert product.price == 5.0


def test_price_setter_lower_with_no(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 5.0
    assert product.price == 10.7


def test_add_product(category):
    new_p = Product("Banana", "Yellow fruit", 8.0, 10)
    category.add_product(new_p)
    assert len(category.products) == 4
    assert category.products[-1].name == "Banana"


def test_list_products(category):
    result = category.list_products
    assert isinstance(result, str)
    assert "Apple, 10.0 руб. Остаток: 5 шт" in result
    assert "Orange, 15.0 руб. Остаток: 3 шт" in result
    assert "Pear, 12.0 руб. Остаток: 4 шт" in result
    assert result.count("\n") == 2


def test_str(category):
    assert str(category) == "Test Category, количество продуктов: 12 шт."


def test_add(category, category_):
    res = category + category_
    assert res == 286


def test_iter_returns_self(category):
    iterator = IterProducts(category)
    assert iter(iterator) is iterator


def test_iter_products_first_item(category):
    iterator = IterProducts(category)
    first = next(iterator)
    assert first.name == "Apple"


def test_iter_products_all_items(category):
    iterator = IterProducts(category)
    names = [next(iterator).name for _ in range(3)]
    assert names == ["Apple", "Orange", "Pear"]


def test_iter_products_all_fields(category):
    iterator = IterProducts(category)
    product = next(iterator)
    assert product.name == "Apple"
    assert product.description == "Red fruit"
    assert product.price == 10.0
    assert product.quantity == 5


def test_iter_stop_iteration(category):
    """После последнего элемента raise StopIteration."""
    iterator = IterProducts(category)
    for _ in range(3):
        next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)


def test_iter_loop(category):
    iterator = IterProducts(category)
    names = [product.name for product in iterator]
    assert names == ["Apple", "Orange", "Pear"]


def test_iter_empty_category():
    empty_cat = Category("Empty", "No products", [])
    iterator = IterProducts(empty_cat)
    with pytest.raises(StopIteration):
        next(iterator)


def test_iter_independent_instances(category):
    iter1 = IterProducts(category)
    iter2 = IterProducts(category)

    next(iter1)
    next(iter1)

    assert next(iter2).name == "Apple"
    assert next(iter1).name == "Pear"
