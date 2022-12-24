from abc import ABC, abstractmethod

"""
    El patron decorator no es lo mismo que la funcion decorador.
    Este patron hace uso de una interface que define la estructura para el Producto y el Decorador,
    La funcion del decorador es agregar funcionanlidad a la clase decorada. pero debe tener la mis
"""

class Elemento(ABC):

    @abstractmethod
    def method(self):
        pass


class Producto(Elemento):

    def method(self):
        print("Ejecutando el metodo del producto")

class ProductoDeco(Elemento):
    
    def method(self):
        print("Ejecutando el metodo del producto deco")

class Decorator(Elemento):

    def __init__(self, elemento_deco):
        self.elemento_deco = elemento_deco

    def method(self):
        print("Ejecutando el metodo del decorador")
        self.elemento_deco.method()


if __name__ == "__main__":
    prod = Producto()
    prod.method()

    deco = Decorator(prod)
    deco.method()

    prod_deco = ProductoDeco()
    deco2 = Decorator(prod_deco)
    deco2.method()


