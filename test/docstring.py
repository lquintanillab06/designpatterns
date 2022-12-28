
def calcular_impuesto(importe: float, impuesto: int):
    """ funcion que calcula el impuesto de una cantidad

    Args:
        importe (float): importe venta
        impuesto (int): impuesto calculado
    Returns: 
        float
    Examples
        >>> calcular_impuesto(100,16)
        16.0
    """
    res = importe * (impuesto / 100)
    return res

if __name__ == "__main__":
    print("Probando el codigo de docstring")

    print(calcular_impuesto.__doc__)

    #help(calcular_impuesto)