



class ProcesadorLegacy():

    def procesar(self,cliente):
        return cliente.data1 / cliente.data2


class ClienteLegacy():

    def __init__(self, data1: int, data2: int):
        self.data1 = data1
        self.data2 = data2

class ClienteModern():

    def __init__(self, data1: str, data2: str):
        self.data1 = data1
        self.data2 = data2

class ClienteAdapter():

    def adapt(self,cliente):
        return ClienteLegacy(int(cliente.data1), int(cliente.data2))




if __name__ == "__main__":
    print("Ejecutando el demo de Adapter")

    cliente = ClienteLegacy(10,2)
    procesador= ProcesadorLegacy()
    print(procesador.procesar(cliente))

    cliente_moderno = ClienteModern("20","10")
    
    # Marca un error porque el procesador legacy trabaja con enteros y enviamos strings
    #print(procesador.procesar(cliente_moderno))
    #se usa el adaptador para cambiar los tipos de los argumentos y sea compatible con el procesador legacy


    adapter = ClienteAdapter()
    cliente_adapted = adapter.adapt(cliente_moderno)
    print(procesador.procesar(cliente_adapted))

