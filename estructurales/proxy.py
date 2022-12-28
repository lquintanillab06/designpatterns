from abc import ABC,abstractmethod

"""
    El patron proxy provee un objeto que sirve como sustituto de un objeto de servicio.
    El proxy recibe la solicitud del cliente realiza operaciones y pasa la solicitud al objeto de servicio
    El objeto proxy tiene la misma interface que el objeto de servicio lo que lo hace intercambiable con un
    objeto real cuando se le pasa al cliente.
"""

class Subject(ABC):

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        print(" Real subject handling a request")

class Proxy(Subject):

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.", end="")


def client_code(subject):
    subject.request()




if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)