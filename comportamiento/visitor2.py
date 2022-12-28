from abc import ABC, abstractmethod

"""
    En el patron visitor se debe definir el metodo accept  en los elementos sobre los que se quiere trabaje el visitor
    el cual recibe una instancia del visitor.
    en el metodo accept se ejecuta un metodo del visitor al que se le pasa la instancia del elemento.
    una vez en el metodo del visitor se puede trabajar con la instancia que se paso sin modificar mucho las clases sobre las que
    se quiere trabaje el visitor.
    Permite añadir nuevos comportamientos a jerarquias o familias de clases.
"""


class Personaje(ABC):

    @abstractmethod
    def accept(self):
        pass

class Guerrero(Personaje):

    def accept(self, visitor):
        visitor.metodo_guerrero(self)


    def ataque_guerrero(self):
        print("Guerrero atacando")


class Mago(Personaje):
    
    def accept(self, visitor):
        visitor.metodo_mago(self)


    def ataque_mago(self):
        print("Mago atacando")


class VisitorPersonaje(ABC):

    @abstractmethod
    def metodo_guerrero(self,personaje):
        pass

    @abstractmethod
    def metodo_mago(self,personaje):
        pass

class VisitorPersonajeA(VisitorPersonaje):

    def metodo_guerrero(self,personaje):
        print("Ejecutando desde el visitor A")
        personaje.ataque_guerrero()

    def metodo_mago(self,personaje):
        print("Ejecutando desde el visitor A")
        personaje.ataque_mago()


class VisitorPersonajeB(VisitorPersonaje):
    
    def metodo_guerrero(self,personaje):
        print("Ejecutando desde el visitor B")
        personaje.ataque_guerrero()

    def metodo_mago(self,personaje):
        print("Ejecutando desde el visitor B")
        personaje.ataque_mago()


if __name__ == "__main__":
    print("Ejecutando el demo de Visitor")
    mago = Mago()
    visitor_a = VisitorPersonajeA()
    mago.accept(visitor_a)
    guerrero = Guerrero()
    guerrero.accept(visitor_a)

    visitor_b = VisitorPersonajeB()
    mago.accept(visitor_b)
    guerrero = Guerrero()
    guerrero.accept(visitor_b)