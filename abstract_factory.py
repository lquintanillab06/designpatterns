from abc import ABC, abstractmethod

"""
    El patron abstract factory se encarga de crear familias de objetos, y crea una interfaz  factory la cual define metodos
    abstractos para crear familias de objetos delegando la creacion de los objetos a clases concretas encargadas de agrupar familias
    de objetos que satisfacen interfaces, cada fabrica se corresponde con una familia de un producto. 
    En el ejemplo declaramos una interfaz para ProductA Papel y ProductB Carton a partir de estas se crean Concrete Products que se 
    corresponden con una familia de Products. Definimos una interface Abstract Factory que declara metodos abstractos para crear objetos
    del tipo ProductA y ProductB. creamos Implementaciones de Abstract Factory que se encargaran de instanciar Concrete ProductA y Concrete ProductB
"""

class Papel(ABC):  
    @abstractmethod
    def create_gramaje(self):
        pass

class Carton(ABC):
    @abstractmethod
    def create_calibre(self):
        pass


class PapelAgua(Papel):
    def create_gramaje(self):
        print("Papel Agua Creado")

class CartonAgua(Carton):
    def create_calibre(self):
        print("Carton Agua Creado")

class PapelPonderosa(Papel):
    def create_gramaje(self):
        print("Papel Ponderosa Creado")

class CartonPonderosa(Carton):
    def create_calibre(self):
        print("Carton Ponderosa Creado")


class AbstractFactory(ABC):
    
    @abstractmethod
    def create_papel(self) :
        pass

    @abstractmethod
    def create_carton(self):
        pass

class AguaFactory(AbstractFactory):
    def create_papel(self):
        return PapelAgua()

    def create_carton(self):
        return CartonAgua()

class PonderosaFactory(AbstractFactory):
    def create_papel(self):
        return PapelPonderosa()

    def create_carton(self):
        return CartonPonderosa()

    
def cliente(factory: AbstractFactory):
    papel = factory.create_papel()
    carton = factory.create_carton()

    papel.create_gramaje()
    carton.create_calibre()


if __name__ == "__main__":
    print("Ejecutando el demo de abstract factory") 
    factory = AguaFactory()
    cliente(factory)

    factory2 = PonderosaFactory()
    cliente(factory2)

