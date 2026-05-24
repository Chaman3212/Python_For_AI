class Product:
    count=0
    def __init__(self,name,price ):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"the product is {self.name} and price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"total product is {cls.count}")

    @staticmethod
    def discount(price , discount):
        final_price = price-(price * discount)/100
        print(f"the final price is {final_price}")



laptop = Product('Hp laptop',20_000)
mobile = Product('Apple mobile',1_00_000)
pen = Product('pen',20)
car = Product('car',20_00_000)

laptop.get_info()
Product.get_count()