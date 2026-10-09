from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    price: float
    quantity: int

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class MixinLog:

    def __init__(self, *args, **kwargs):
        self.saved_args = args
        self.saved_kwargs = kwargs
        super().__init__(*args, **kwargs)

    def __repr__(self):
        args_str = ", ".join(repr(args) for args in self.saved_args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in self.saved_kwargs.items())
        all_parts = [args_str, kwargs_str]
        params = ", ".join(p for p in all_parts if p)
        return f"{self.__class__.__name__}({params})"


class Product(MixinLog, BaseProduct):

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Складывать можно только экземпляры класса Product")
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

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            return "Складывать можно только экземпляры класса Product"

    @property
    def products_list(self):
        return self.__products

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)


class IterProducts:
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        products = self.category.products_list
        if self.index >= len(products):
            raise StopIteration
        product = products[self.index]
        self.index += 1
        return product
