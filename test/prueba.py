
def calcular_impuesto(importe: float, impuesto: int):
    """ funcion que calcula el impuesto de una cantidad

    Args:
        importe (float): importe venta
        impuesto (int): impuesto calculado
    Returns: 
        float
      
    """
    res = importe * (impuesto / 100)
    return res

if __name__ == "__main__":
    print("Probando el codigo de docstring")