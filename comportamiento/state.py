from abc import ABC, abstractmethod

class Surtido():
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
        A reference to the current state of the Context.
    """

    def __init__(self, state) :
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def recolectado(self):
        self._state.handle1()

    def cortado(self):
        self._state.handle2()

    def get_state(self):
        return self._state.name


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) :
        return self._context

    @context.setter
    def context(self, context) :
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass


class Recoleccion(State):

    def __init__(self) :
        self.name = "Recoleccion"
        

    def handle1(self):
        print("Recoleccion handles recoleccion.")
        print("Recoleccion wants to change the state of the context.")
        self.context.transition_to(Corte())

    def handle2(self):
        print("Recoleccion handles request2.")


class Corte(State):
    def __init__(self) :
        self.name = "Corte"

    def handle1(self):
        print("Corte handles request1.")

    def handle2(self):
        print("Corte handles corte.")
        print("Corte wants to change the state of the context.")
        self.context.transition_to(Recoleccion())


if __name__ == "__main__":
    print("Ejecutando el demo de State")

    recoleccion = Recoleccion()
    surtido = Surtido(recoleccion)
    print("**",surtido.get_state())
    surtido.recolectado()
    print("**",surtido.get_state())
    surtido.cortado()
    print("**",surtido.get_state())
    
   