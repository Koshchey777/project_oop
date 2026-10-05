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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.price * other.quantity)

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

    def __str__(self):
        res = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {res} шт."

    def add_product(self, Product):
        self.__products.append(Product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def list_products(self):
        return "\n".join(str(product) for product in self.__products)


class IterProducts:
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
