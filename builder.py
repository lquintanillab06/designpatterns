from abc import ABC,abstractmethod

"""
    Este patron sinve para construir objetos complejos paso a paso, se define una interfaz builder la cual se emplea en el caso 
    de cuando queremos construir mas objetos con la misma estructura, se define un Concrete Buuilder el cual se va a encargar de 
    implementar los metodos para construir un producto en particular y por ultimo se define una clase Director la cual va a determinar 
    el orden y como se va a construir el Producto.
    En el ejemplo se define una interfaz Builder y una clase ComprobanteBuilder que implementa Builder, tenemos una clase Comprobante que
    es el objeto complejo que vamos a construir, y una clase Director que es la encargada de determinar como se va a construir el objeto 
    Comprobante determinando el orden y las partes a construir 
"""


class Builder(ABC):

    ''' @property
    @abstractmethod
    def comprobante(self):
        pass '''

    @abstractmethod
    def build_emisor(self):
        pass

    @abstractmethod
    def build_receptor(self):
        pass

    @abstractmethod
    def build_nodo1(self):
        pass

class ComprobanteBuilder(Builder):
    
    def __init__(self):
        self.comprobante = Comprobante()

    def build_emisor(self):
        self.comprobante.emisor = "Papel"
        return self

    def build_receptor(self):
        self.comprobante.receptor = "Impap"
        return self

    def build_nodo1(self):
        self.comprobante.nodo1 = "Nodo1"
        return self

    def get_comprobante(self):
        return self.comprobante

class Comprobante():
    def __init__(self):
        self.receptor = None
        self.emisor = None
        self.nodo1= None


class Director():


    def __init__(self, builder):
        self.builder = builder

    def create_medium(self):
       
       return self.builder.build_emisor().get_comprobante()

    def create_full(self):
        return self.builder.build_emisor().build_receptor().get_comprobante()
    
    def create_with_nodo1(self):
        return self.builder.build_emisor().build_receptor().build_nodo1().get_comprobante()   


def cliente(builder):
    
    director = Director(builder)
    medium = director.create_medium()
    print(medium.__dict__)

def cliente2(builder):
    
    director = Director(builder)
    medium = director.create_full()
    print(medium.__dict__)

def cliente3(builder):
    
    director = Director(builder)
    medium = director.create_with_nodo1()
    print(medium.__dict__)


if __name__ == "__main__":

    builder = ComprobanteBuilder()

    cliente(builder)

    cliente2(builder)

    cliente3(builder)