from abc import ABC, abstractmethod


class ModernInteface(ABC):
    @abstractmethod
    def method_modern(self):
        pass

class LegacyInterface(ABC):
    @abstractmethod
    def method_legacy(self):
        pass


class Modern(ModernInteface):
    def method_modern(self):
        print("Running method modern")

class Legacy(LegacyInterface):
    def method_legacy(self):
        print("Running method legacy")


class ModernAdapater(LegacyInterface):

        def __init__(self, adapte):
            self.adapte = adapte

        def method_legacy(self):
            print("Running method adapter")
            self.adapte.method_modern()

def cliente(legacy):
    legacy.method_legacy()


if __name__ == "__main__":
    print("Ejecuntado el Demo  Adapter ")
    legacy = Legacy()
    cliente(legacy)
    modern = Modern()
    adaptee = ModernAdapater(modern)
    cliente(adaptee)


