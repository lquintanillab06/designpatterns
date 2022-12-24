from abc import ABC, abstractmethod


# Interfaz Implementacion
class Color(ABC):

    @abstractmethod
    def get_color(self):
        pass

# Implementaciones Concretas
class Rojo(Color):

    def get_color(self):
        return "Rojo"

class Azul(Color):
    
    def get_color(self):
        return "Azul"

class Verde(Color):
    
    def get_color(self):
        return "Verde"

# Interfaz abstraccion
class Forma(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def get_color(self):
        pass

# Abstracciones Concretas
class Esfera(Forma):
    def tipo(self):
        print("Trabajando en una esfera")

    def get_color(self):
        color_applied = self.color.get_color()
        print(f"Aplicando el color {color_applied}")
        

class Cubo(Forma):
    def tipo(self):
        print("Trabajando en un cubo")

    def get_color(self):
        color_applied = self.color.get_color()
        print(f"Aplicando el color {color_applied}")

# Cliente
def cliente(forma: Forma):
    
   
    forma.tipo()
    forma.get_color()

if __name__ == "__main__":

    rojo = Rojo()
    cubo = Cubo(rojo)
    esfera = Esfera(rojo)

    cliente(cubo)
    cliente(esfera)

    azul = Azul()
    cubo_azul = Cubo(azul)
    esfera_azul = Esfera(azul)

    cliente(cubo_azul)
    cliente(esfera_azul)

    verde = Verde()
    cubo_verde = Cubo(verde)
    esfera_verde = Esfera(verde)

    cliente(cubo_verde)
    cliente(esfera_verde)