from abc import ABC, abstractmethod

"""
    El patron facade es un patron estructural que proporciona una interfaz simplificada a una biblioteca, un framework  o
    cualquier otro grupo complejo de clases.
    Un facade nos sirve para cuando tenemos un gran numero de funciones pero solo necesitamos usar unas cuantas
    funciones.
"""

class Subsystem1():

    def operation1(self):
        print("Ejecutando la operacion 1 del subsistema 1")

    def operation2(self):
        print("Ejecutando la operacion 2 del subsistema 1")

class Subsystem2():
    
    def operation3(self):
        print("Ejecutando la operacion 3 del subsistema 2")

    def operation4(self):
        print("ejecutando la operacion 4 del subsistema 2")

class Facade():

    def __init__(self, subsystem1, subsystem2):

        self.subsystem1 =  subsystem1
        self.subsystem2 = subsystem2

    def operation_facade(self):
        self.subsystem1.operation1()
        self.subsystem1.operation2()
        self.subsystem2.operation3()
        self.subsystem2.operation4()


def cliente(facade):
    facade.operation_facade()


if __name__ == "__main__":
    
    system1 = Subsystem1()
    system2 = Subsystem2()

    facade = Facade(system1, system2)

    cliente(facade)


    