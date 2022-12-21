from abc import ABC, abstractmethod

class DigitalCoinProcessor():
    @abstractmethod
    def predict(cls):
        pass

class BitCoinProcessor():
    def predict(self):
        print("Procesando Bit Coin")

class EthereumProcessor():
    def predict(self):
        print("Procesando Ethereum")


class FactoryDigitalProcessor():
    

    def create_processor(self, clave):

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
