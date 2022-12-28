from abc import ABC,abstractmethod

class Descuento():

    def __init__(self, strategy):
        self._strategy = strategy
        self.importe = 0.00

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def calcular_descuento(self):
        print("Calculando el descuento")

        descuento = self.strategy.calcular(self.importe)
        return descuento



class DescuentoStrategy(ABC):

    @abstractmethod
    def calcular(self):
        pass

class DescuentoOrdinario(DescuentoStrategy):

    def calcular(self,importe):
        print("Aplicando el descuento ordinario del 10%")        
        return importe * .10


class DescuentoNavidad(DescuentoStrategy):
    
    def calcular(self,importe):
        print("Aplicando el descuento Navidad del 30%")        
        return importe * .30


if __name__ == "__main__":
    print("Ejecutando el demo de Strategy")
    descuento_ord = DescuentoOrdinario()
    descuento = Descuento(descuento_ord)
    descuento.importe = 1000

    res = descuento.calcular_descuento()
    print(res)

    print("Cambiando el Descuento")
    descuento_nav = DescuentoNavidad()
    descuento.strategy = descuento_nav
    res = descuento.calcular_descuento()
    print(res)

