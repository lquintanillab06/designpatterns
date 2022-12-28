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
    # Invoker

    commands = {}

    def add_command(self,key, command):
        self.commands[key] = command
        

    def get_command(self,key):
        command = self.commands.get(key)
        if not command:
            print("Comando no encontrado !!!")
        return command

    def remove_command(self, key):
       del self.commands[key]

    def execute_command(self,key):
        #command = self.commands.get(key)
        command = self.get_command(key)
        if not command:
            print("Comando no soportado !!!")
            return
        command.execute()



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


if __name__ == "__main__":
    print("Corriendo el demo de Command")

    luz = Luz()
    luz_on = CommandLuzOn(luz)
    luz_off = CommandLuzOff(luz)
    control = ControlInteligente()
    control.add_command('luz_on',luz_on)
    control.add_command('luz_off',luz_off)
    print(control.commands)
    control.execute_command('luz_on')
    control.execute_command('luz_off')
    bocina = Bocina()
    bocina_up = CommandBocinaUp(bocina)
    bocina_down = CommandBocinaDown(bocina)
    control.add_command('bocina_up', bocina_up)
    control.add_command('bocina_down', bocina_down)
    print(control.commands)
    control.execute_command('bocina_up')
    control.execute_command('bocina_down')
    control.remove_command('bocina_up')
    control.remove_command('bocina_down')
    print(control.commands)

    control.execute_command('bocina_down')



        
        