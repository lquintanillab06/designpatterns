

from abc import ABC, abstractmethod
from enum import Enum

class Niveles(Enum):
    N1 = 1
    N2 = 2
    N3 = 3



class Request():
    
    def __init__(self,nivel ,numero1,numero2):
        self.nivel = nivel
        self.numero1 = numero1
        self.numero2 = numero2

class Handler(ABC):
    
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request,previous = 0):
        pass

class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler):
        self._next_handler = handler 
        return handler

    @abstractmethod
    def handle(self, request, previous = 0):
        if self._next_handler:
            return self._next_handler.handle(request, previous)

        return None


class N1Handler(AbstractHandler):
    
    def handle(self, request, previous = 0):
        if request.nivel.value >= 1 :
            res =  previous + request.numero1 + request.numero2
            print("***",res)
            if request.nivel.value == 1 :
                return res
            else:
                super().handle(request,res)
            
        else:
            return super().handle(request)


class N2Handler(AbstractHandler):
    
    def handle(self, request,previous = 0):
        if request.nivel.value >= 2 :
            res =  previous * request.numero1 * request.numero2
            print("***",res)
            if request.nivel.value == 2 :
                return res
            else: 
                super().handle(request,res)
        else:
            return super().handle(request)

class N3Handler(AbstractHandler):
    
    def handle(self, request,previous = 0):
        if request.nivel.value >= 3 :
            res =  previous - request.numero1 - request.numero2
            print("***",res)
            if request.nivel.value == 3 :
                return res
            else:
                super().handle(request,res)
        else:
            return super().handle(request)


def cliente(handler,request):
    
    result = handler.handle(request)

    print(result)

if __name__ == "__main__":
    
    request = Request(Niveles.N3, 5,10)

    print(request.nivel.value)

    n1 = N1Handler()
    n2 = N2Handler()
    n3 = N3Handler()

    n1.set_next(n2).set_next(n3)

    print("Chain: n1 > n2 > n3")
    cliente(n1,request)
    print("\n")

