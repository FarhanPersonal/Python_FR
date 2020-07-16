class Product: 
    def __init__(self, price):
        self.cost=price
        
    @property
    def cost(self): 
        return self.__price

    @cost.setter
    def cost(self, value):
        if value <0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    

product = Product(30)
product.cost=100

print(product.cost)

