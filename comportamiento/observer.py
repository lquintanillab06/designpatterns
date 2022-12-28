
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass


class Venta(Subject):

    productos= []
    folio = 0

    observers = []

    def attach(self, observer):
        print("Subject: Attached an observer.")
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    
    def notify(self):
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self.observers:
            observer.listen(self)

    def add_producto(self, producto):
        self.productos.append(producto)

    def sale(self):
        if not len(self.productos):
            print("No hay productos para vender")
            return
        self.folio=1000
        self.notify()

    def show_productos(self):
        print(self.productos)



class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def listen(self, subject):
        """
        Receive update from subject.
        """
        pass

class ExistenciaObserver(Observer):

    def listen(self, subject):
       for producto in subject.productos:
            print(f"Actualizando la existencia de {producto}")

class OrdenSurtidoObserver(Observer):
    
    def listen(self, subject):
        print(f"Generando Orden de surtido para la venta {subject.folio}")
        for producto in subject.productos:
            print(f"Registrando en la orden de surtido {producto}")



if __name__ == "__main__":
    print("Ejecutando el demo de Observer")

    venta = Venta()
    venta.sale()

    existencia_observer = ExistenciaObserver()
    orden_observer = OrdenSurtidoObserver()

    venta.attach(existencia_observer)
    venta.attach(orden_observer)

    venta.add_producto('POL100')
    venta.add_producto('POL75')
    venta.show_productos()

    venta.sale()