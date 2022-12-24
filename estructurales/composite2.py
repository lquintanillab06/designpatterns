from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self,tipo):
        self.tipo = tipo


    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent):
        self.parent = parent

  
    def add(self):
        pass


    def remove(self):
        pass

    @abstractmethod
    def operation(self):
        pass

    def is_composite(self):
        return False

class Producto(Component):

    def __init__(self, tipo):
        super().__init__(tipo)

    def operation(self):
        print("Este es un producto !!!")

class Caja(Component):

    def __init__(self,tipo):
        self.contenido = []
        super().__init__(tipo) 


    def add(self, component: Component):
        self.contenido.append(component)
        #component.parent = self.tipo

    def remove(self, component):
        self.contenido.remove(component)
        component.parent = None

    def is_composite(self):
        return True
    
    def operation(self):
        print(f"Esta es una caja y contiene {self.contenido}")


def cliente_code(component):

    component.operation()

def cliente_code2(component1, component2):

    if component1.is_composite():
        component1.add(component2)
        component1.operation()

if __name__  == "__main__":

    prd = Producto("prd")
    #cliente_code(comp)

    prd2 = Producto("prd1") 

    caja1 = Caja("caja1")
    caja2 = Caja("caja2")
    #cliente_code(comp2)
    prd3 = Producto("prd3") 
    prd4 = Producto("prd4") 
    caja3 = Caja("Caja3")

    cliente_code2(caja1,prd)
    cliente_code2(caja1,prd2)
    cliente_code2(caja2,prd3)
    cliente_code2(caja2,prd4)
    cliente_code2(caja1,caja2)
    cliente_code2(caja1,caja3)
    
    print(caja1.contenido)
    print (caja1.contenido[2].contenido[0].tipo)
    print (caja1.contenido[2].contenido[1].tipo)
    print (caja1.contenido[2].tipo)
    print (caja1.contenido[0].tipo)
    print (caja1.contenido[1].tipo)

    print("*"*100)
    for comp in caja1.contenido:
        
        if comp.is_composite():
            print(f"Es una caja {comp.tipo}")
            print(comp.contenido)
        else:
            print(f"Es un producto {comp.tipo}")
    
    

