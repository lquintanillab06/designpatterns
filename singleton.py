"""
El patron singleton sirve para restringir la creacion de instancias de objetos a una unica instancia.
Con el objetivo de optimizar recursos como el uso de memoria utilizada por el programa al crear instancias
Tambien para tener una unica instancia que mantenga el estado para todos aquellos objetos que requieran usarla.
"""


class SingletonMeta(type):


    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Ejecutando codigo del singleton")

class Singleton2(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("Ejecutando codigo del singleton")
        



if __name__ == "__main__":

    # The client code.

    s1 = Singleton2()
    s2 = Singleton2()

    if id(s1) == id(s2):
        print("Singleton correcto, ambas variables contienen la misma instancia")
    else:
        print("Singleton fallo, variables contienen diferentes instancias ")
  