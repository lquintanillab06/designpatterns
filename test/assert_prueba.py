

def sumar_dos_numeros(n1,n2):
    """Funcion que suma dos números positivos.

    Args:
        n1 (int): numero1
        n2 (int): numero2
    """
    try:
        assert n1 >0 and n2 >0, "Lo sentimos los numeros deben ser positivos"
        return n1 + n2
    except AssertionError as error:
        print(error)

if __name__ == "__main__":

    print("Ejecutando el demo de assert")
    print(sumar_dos_numeros(-3,4))


