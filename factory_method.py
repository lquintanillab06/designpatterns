from abc import ABC, abstractmethod

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

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self):
        return AirPlane()

class Transport(ABC):
    @abstractmethod
    def delivery(self):
        pass

class Truck(Transport):

    def delivery(self):
        print("Realizando la entrega en camion...")

class Ship(Transport):
    
    def delivery(self):
        print("Realizando la entrega en Bote...")

class AirPlane(Transport):
    def delivery(self):
        print("Realizando la entrega en Avion...")

def cliente_logistics(logistics : Logistics):

    logistics.plan_delivery()
    transport = logistics.create_transport()
    transport.delivery()


if __name__ == "__main__":
    print("Corriendo el demo de Factory Method")

    cliente_logistics(SeaLogistics())
    cliente_logistics(RoadLogistics())
    cliente_logistics(AirLogistics())


   
   



    