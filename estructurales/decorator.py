from abc import ABC, abstractmethod

class Elemento(ABC):

    @abstractmethod
    def method(self):
        pass


class Producto(Elemento):

    def method(self):
        print("Ejecutando el metodo del producto")

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
