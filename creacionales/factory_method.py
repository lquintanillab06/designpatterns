from abc import ABC, abstractmethod

"""
    El patron factory metod hace uso de una clase abstracta o interface Creator que define un metodo abstracto para crear objetos y las clases Concrete Creator 
    que implementan Creator se encargaran de instanciar un objeto Concrete Product que implementan una interface Product.
    El cliente ocupara objetos del tipo de la interface Creator y Product.
    En el ejemplo de Logistics se define la interface Logistics con el metodo abstracto create_transport, definimos las clases concretas
    RoadLogistics y SeaLogistic que implementan el metodo create_transport en el cual creamos una instancia de Truck o Ship que tambien
    implementan una interfaz Transport.
    El código que utiliza el método fábrica (a menudo denominado código cliente) no encuentra diferencias entre los productos devueltos 
    por varias subclases, y trata a todos los productos como la clase abstracta Transporte. El cliente sabe que todos los objetos de transporte
     deben tener el método entrega, pero no necesita saber cómo funciona exactamente.

"""

class ProcessorFactory(ABC):
    @abstractmethod
    def create_processor(self):
        pass
    
class BitCoinProcessorFactory(ProcessorFactory):
    def create_processor(self):
        return BitCoinProcessor()

class EtheremProcessorFactory(ProcessorFactory):  
    def create_processor(self):
        return EthereumProcessor()

class CryptoProcessor(ABC):
    @abstractmethod
    def predict(self):
        pass

class BitCoinProcessor(CryptoProcessor):
    def predict(self):
        print("Procesando Bit Coin")

class EthereumProcessor(CryptoProcessor):
    def predict(self):
        print("Procesando Ethereum")


def cliente_crypto():
    btcFactory = BitCoinProcessorFactory()
    btc = btcFactory.create_processor()
    btc.predict()

    ethFactory = EtheremProcessorFactory()
    eth = ethFactory.create_processor()
    eth.predict()



class Logistics(ABC):

    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        print("Planificando la entrega")

class Transport(ABC):
    @abstractmethod
    def delivery(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) :
        return Ship()

''' class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return AirPlane() '''



class Truck(Transport):

    def delivery(self):
        print("Realizando la entrega en camion...")

class Ship(Transport):
    
    def delivery(self):
        print("Realizando la entrega en Bote...")

''' class AirPlane(Transport):
    def delivery(self):
        print("Realizando la entrega en Avion...") '''

def cliente_logistics(logistics : Logistics):

    logistics.plan_delivery()
    transport = logistics.create_transport()
    transport.delivery()


if __name__ == "__main__":
    print("Corriendo el demo de Factory Method")

    cliente_logistics(SeaLogistics())
    cliente_logistics(RoadLogistics())
    ''' cliente_logistics(AirLogistics()) '''


   
   



    