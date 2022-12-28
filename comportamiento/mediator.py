from abc import ABC, abstractmethod

"""
    Este patron sirve para reducir la dependencia entre los componentes y forza a que la iteraccion entre componentes sea
    atravez de un objeto mediador, cada componente debe recibir una instancia del mediador que tienen un metodo notify el cual
    se ocupara para decirle al mediador que el componente ya realizo su tarea y que proceda a notificarle a otro componente
    para que este realice su tarea.
    El mediador debe tener instancias de los componentes de los cuales se va a encargar de mediar.
"""

class Mediator(ABC):
    @abstractmethod
    def notify():
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent():

    def __init__(self, mediator = None):
        self.mediator = mediator
    
    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self) :
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")
        self.mediator.notify(self, "B")
    
class Component2(BaseComponent):
    
    def do_c(self):
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")







if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()