class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, goods_list: list):
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        for product in goods_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Цена ниже изначальной. Оставить новую цену? y/n\n")
            if answer == "y":
                self.__price = value
        else:
            self.__price = value


class Category:
    products: list[Product]
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, Product):
        self.__products.append(Product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def list_products(self):
        result = []
        for i in self.__products:
            price = i.price
            name = i.name
            rest = i.quantity
            result.append(f'{name}, {price} руб. Остаток: {rest} шт')
        return '\n'.join(result)
