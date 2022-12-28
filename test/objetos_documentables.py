"""
    Este es el doctstring del modulo
    Los objetos documentables son los Modulos, Clases, Metodos y Funciones.
"""

class User():
    """Este es el Docstring de la clase
    """

    def metodo(self, username, password):
        """Este es el docstring del metodo
        """
        print(username)
        print(password)


if __name__ == "__main__":
    # El docstring del modulo se obtiene desde fuera del modulo
    #print(objetos_documentables.__doc__)
    print(User.__doc__)
    print(User.metodo.__doc__)

    