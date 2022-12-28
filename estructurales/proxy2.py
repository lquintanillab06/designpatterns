from abc import ABC, abstractmethod
import datetime


class Informacion(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass

class InformacionReal(Informacion):

    def mostrar_informacion(self):
        print("Mostrando informacion real")

class InformacionProxy(Informacion):

    def __init__(self,informacion_real):

        self.informacion_real = informacion_real

    def mostrar_informacion(self):
            self.log_acces()
            self.informacion_real.mostrar_informacion()
            self.log_acces()
    
    def log_acces(self):
        print(datetime.datetime.now())


def cliente(informacion):

    informacion.mostrar_informacion()


if __name__ == "__main__":
    informacion_real = InformacionReal()
    informacion = InformacionProxy(informacion_real)

    cliente(informacion_real)
    cliente(informacion)
