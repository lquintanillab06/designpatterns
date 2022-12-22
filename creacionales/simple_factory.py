from abc import ABC, abstractmethod
"""
    El patron simple factory se usa para crear instancias de objetos que comparten una interfaz,  se define una clase factory la
    cual se va a encargar de instanciar el objeto segun se requiera por el cliente.
    En el ejemplo se define una interfaz para Product y n clases concretas que implementan Product a las cuales les conocemos como
    Concrete Product, despues se define una clase factory que se encargará de instanciar un Concrete Product determinado por un bloque
    de condiciones de tipo. para este caso se puede usar enumeraciones para delimitar los tipos.
    
"""

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