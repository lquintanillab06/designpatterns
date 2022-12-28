from abc import ABC, abstractmethod


class Exportador(ABC):

    def exportador_template(self):
        self.get_remote_conexion()
        self.get_local_conexion()
        self.read_data()
        self.clean_data()
        self.prepare_data()
        self.export_data()
        self.data_disperse()


    def get_remote_conexion(self):
        print("Obteniendo Conexion remota ...")

    def get_local_conexion(self):
        print("Obteniendo Conexion local ...")

    def read_data(self):
        print("Leyendo datos ...")

    @abstractmethod
    def clean_data(self):
        pass

    @abstractmethod
    def prepare_data(self):
        pass

    def export_data(self):
        print("Exportando los datos")

    def data_disperse(self):
        pass


class ExportadorDepositos(Exportador):

    def clean_data(self):
        print("Limpiando los datos en el Exportador de Depositos")

    def prepare_data(self):
        print("Preparando los datos en el Exportador de Depositos")


class ExportadorExistencia(Exportador):
    
    def clean_data(self):
        print("Limpiando los datos en el Exportador de Existencia")

    def prepare_data(self):
        print("Preparando los datos en el Exportador de Existencia")

    def data_disperse(self):
        print("Dispersando la informacion a sucursales")


def cliente(exportador):

    print("*"*100)
    exportador.exportador_template()



if __name__ == "__main__":
    print("Ejecutando el demo de Template Method")


    exportador_exis = ExportadorExistencia()

    cliente(exportador_exis)

    exportador_depo = ExportadorDepositos()
    cliente(exportador_depo)

