from abc import ABC, abstractmethod
#https://www.youtube.com/watch?v=iz8U8noXNqs

class Luz():
    # Receiver

    def on(self):
        print("Encendiendo la luz")

    def off(self):
        print("Apagado la luz")

class TV():
    #Receiver
    
    def on(self):
        print("Encendiendo la TV")

    def off(self):
        print("Apagado la TV")

class Bocina():
    # Receiver

    def up(self):
        print("Subiendo el volumen")

    def down(self):
        print("Bajando el volumen")


class ControlInteligente():

    commands = {}

    def add_command(self):
        pass

    def get_command(self,command):
        pass

    def remove_command(self):
        pass

    def execute_command(self,command):
        pass



class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class CommandLuzOn(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.on()

class CommandLuzOff(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.off()

class CommandBocinaUp(Command):
    def __init__(self, bocina):
        self.bocina = bocina

    def execute(self):
        self.bocina.up()
    
class CommandBocinaDown(Command):
    def __init__(self, bocina):
        self.bocina = bocina

    def execute(self):
        self.bocina.down()
        
        