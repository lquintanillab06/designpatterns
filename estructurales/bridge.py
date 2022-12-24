from abc import ABC, abstractmethod

"""
    El patron Bridge una clase grande o un grupo de clases estrechamente ligadas en dos jerarquias (Abstraccion e Implementacion)
    cabe recalcar que no hace referencia a los conceptos de POO se refiere a Jerarquias donde Abstraccion es el pivote que por medio 
    de la composicion se le agregaran funciones por medio de las clases concretas de la Implementación.
    Este patron nos evita el crecimiento exponencial, ya que si requerimos agregar una implementacion no es necesario crear una clase
    que contenga todo solo es necesario agregar a la abstraccion la nueva implementacion
"""


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class Abstraction():
    def __init__(self, implementation: Implementation):
            self.implementation = implementation

    def operation(self) :
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

class ExtendAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")





class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendAbstraction(implementation)
    client_code(abstraction)