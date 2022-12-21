from abc import ABC, abstractmethod

class DigitalCoinProcessor(ABC):
    @abstractmethod
    def predict(cls):
        pass

class BitCoinProcessor(DigitalCoinProcessor):
    def predict(self):
        print("Procesando Bit Coin")

class EthereumProcessor(DigitalCoinProcessor):
    def predict(self):
        print("Procesando Ethereum")


class FactoryDigitalProcessor():
    
    def create_processor(self, clave):
        if clave == 'BTC':
            return BitCoinProcessor()
        if clave == 'ETH':
            return EthereumProcessor()

class FactoryProcessor():
    """ 
        Patron simple factory usando metodos estaticos
    """
    @staticmethod
    def create_processor(clave):
        if clave == 'BTC':
            return BitCoinProcessor()

        if clave == 'ETH':
            return EthereumProcessor()


if __name__ == "__main__":

    factory = FactoryDigitalProcessor()
    btc = factory.create_processor('BTC')
    btc.predict()
    eth= factory.create_processor('ETH')
    eth.predict()
    btc2= FactoryProcessor.create_processor('BTC')
    btc2.predict()