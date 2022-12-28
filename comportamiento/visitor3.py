from abc import ABC, abstractmethod

class Area(ABC):
    # Interface Component

    @abstractmethod
    def accept(self, visitor):
        pass

class ZonaArqueologica(Area):
    # Component Concreto

    def __init__(self):
        self.name = "ZA"

    def accept(self,exportador):
        exportador.exportar_zona_arqueologica(self)

class ZonaDeportiva(Area):
    # Component Concreto

    def __init__(self):
        self.name = "ZD"

    def accept(self,exportador):
        exportador.exportar_zona_deportiva(self)

class Exportador(ABC):
    # Interface Visitor

    @abstractmethod
    def exportar_zona_arqueologica(self,zona):
        pass

    @abstractmethod
    def exportar_zona_deportiva(self,zona):
        pass

class ExportadorXML(Exportador):
    # Visitor Concreto

    def exportar_zona_arqueologica(self,zona):
        print(f"Exportando a XML {zona.name}")
    
    def exportar_zona_deportiva(self,zona):
        print(f"Exportando a XML {zona.name}")


class ExportadorJSON(Exportador):
    # Visitor Concreto

    def exportar_zona_arqueologica(self,zona):
        print(f"Exportando a JSON {zona.name}")
    
    def exportar_zona_deportiva(self,zona):
        print(f"Exportando a JSON {zona.name}")


if __name__ == "__main__":
    print("Ejecutando el demo de visitor")

    xml = ExportadorXML()
    json = ExportadorJSON()
    za = ZonaArqueologica()
    zd = ZonaDeportiva()
    za.accept(xml)
    zd.accept(xml)
    za.accept(json)
    zd.accept(json)



        