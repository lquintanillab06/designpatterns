
class ProductExceptionError(Exception):
    pass


class Product():
    
    def __init__(self, name , price, discount):
        self.name = name
        self.price = price
        self.discount = discount

        if discount > price:
            raise ProductExceptionError("El descuento no puede ser mayor al precio")


