def test_init_smartphone(example_smartphone):
    assert example_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert example_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert example_smartphone.price == 180000.0
    assert example_smartphone.quantity == 5
    assert example_smartphone.efficiency == 95.5
    assert example_smartphone.model == "S23 Ultra"
    assert example_smartphone.memory == 256
    assert example_smartphone.color == "Серый"
