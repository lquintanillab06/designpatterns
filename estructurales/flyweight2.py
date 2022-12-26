
class BulletGunFW():
    
    def __init__(self,state):
        self.tamaño = state[0]
        self.color = state[1]
        self.daño = state[2]

    def shoot(self, objetivo):
        print(f"Disparando BulletGun causando un {self.daño} de daño al objetivo {objetivo} ")


class BulletGunFactory():

    bullets = {}

    def __init__(self, initial_bullets):
        for state in initial_bullets:
            self.bullets[self.get_key(state)] = BulletGunFW(state)

    def get_key(self, state):
        """
        Returns a Flyweight's string hash for a given state.
        """
        return "_".join(sorted(state))


    def get_bullet(self, shared_state):
        """
            Returns an existing Flyweight with a given state or creates a new one.
        """

        key = self.get_key(shared_state)

        if not self.bullets.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self.bullets[key] = BulletGunFW(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self.bullets[key]

    def list_bullets(self):
        count = len(self.bullets)
        print(f"BulletGunFactory: I have {count} bullets:")
        print("\n".join(map(str, self.bullets.keys())), end="")




if __name__ == "__main__":

    """
        El BulletGunFactory se encarga de construir objetos del tipo BulletGunFW que es el objeto Flyweight, normalmente 
        se hace una precarga de los elementos comunmente usados, el factory tiene un metodo que busca dentro del estado
        inicial el BulletGunFW solicitado si lo encuentra lo devuelve si no esta lo crea.
        Una vez que se tiene el BulletGunFW se le envia la data que corresponde al estado que cambia.
        Al estado inicial se le conoce como estado intrinseco y al cambiante se le conoce como estado extrinseco.
    """
    factory = BulletGunFactory([['5','rojo','15'],['10','azul','30'],['15','gris','45']])
    #factory.list_bullets()
    #tirador(factory,'20','rojo','50','malo1')
    #factory.list_bullets()
    bullet = factory.get_bullet(['5','rojo','15'])
    print(bullet)
    print(bullet.__dict__)
    bullet.shoot('malo1')
    bullet.shoot('malo2')
    
    bullet2 = factory.get_bullet(['25','rojo','60'])
    print(bullet2)
    print(bullet2.__dict__)
    bullet2.shoot('malo1')
    bullet2.shoot('malo2')  

    factory.list_bullets() 