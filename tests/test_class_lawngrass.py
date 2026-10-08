def test_init_lawngrace(example_grass):
    assert example_grass.name == "Газонная трава"
    assert example_grass.description == "Элитная трава для газона"
    assert example_grass.price == 500.0
    assert example_grass.quantity == 20
    assert example_grass.country == "Россия"
    assert example_grass.germination_period == "7 дней"
    assert example_grass.color == "Зеленый"
