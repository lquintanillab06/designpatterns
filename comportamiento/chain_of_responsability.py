from abc import ABC, abstractmethod
from enum import Enum

class Tipos(Enum):
    SUMA = 'SUMA'
    RESTA = 'RESTA'
    MULTIPLICACION = 'MULTIPLICACION'

class Request():

    def __init__(self,tipo: Tipos,numero1,numero2):
        self.tipo = tipo
        self.numero1 = numero1
        self.numero2 = numero2
    
    
class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class SumaHandler(AbstractHandler):

    def handle(self, request):
        if request.tipo == Tipos.SUMA:
            return f"Atendido por Suma Handler Resultado = {request.numero1 + request.numero2}"
        else:
            return super().handle(request)

class MultiplicacionHandler(AbstractHandler):
    
    def handle(self, request):
        if request.tipo == Tipos.MULTIPLICACION:
            return f"Atendido por Multiplicacion Handler Resultado = {request.numero1 * request.numero2}"
        else:
            return super().handle(request)

class RestaHandler(AbstractHandler):
    
    def handle(self, request):
        if request.tipo == Tipos.RESTA:
            return f"Atendido por Resta Handler Resultado = {request.numero1 - request.numero2}"
        else:
            return super().handle(request)

def cliente(handler,request):
    
    result = handler.handle(request)

    print(result)


if __name__ == "__main__":

    request = Request(Tipos.MULTIPLICACION, 5,10)

    print(request.tipo)

    suma = SumaHandler()
    resta = RestaHandler()
    multiplicacion = MultiplicacionHandler()

    suma.set_next(resta).set_next(multiplicacion)

    print("Chain: suma > resta > multiplicacion")
    cliente(suma,request)
    print("\n")


    print("Chain: resta > multiplicacion")
    cliente(resta,request)
    print("\n")
