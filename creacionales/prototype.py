
import copy

"""
    El patron prototype nos permite hacer copias o clones de objetos preconfigurados sin conocer su implementacion concreta.

"""

class SomeComponent():

    def __init__(self):
        print("Incializando Some Component")


    def __copy__(self):
        print("Copiando Some Component") 

    def __deepcopy__(self,memo=None):
        print("Copiando Some Component en profundidad")



if __name__ == "__main__":

    print("Ejecutando el demo de Prototype")

    some = SomeComponent()

    copy.copy(some)
    copy.deepcopy(some)