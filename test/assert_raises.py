import unittest
from product import Product, ProductExceptionError

"""
    Al guardar las pruebas en un modulo podemos ejecutar todo el modulo y esto ejecutara todas las pruebas dentro del modulo,
    tambien se pueden ejecutar las pruebas para una clase de test  o un metodo en particular.
    >>> python -m unittest -v modulo.py
    >>> python -m unittest -v modulo.py.Clase
    >>> python -m unittest -v modulo.py.Clase.metodo

    Para validar la cobertura del codigo se usa
    >>> coverage run -m unittest  libreria_unittest.py 
    >>> coverage run -m unittest  discover
"""
 

def available_to_skip():
    return False

class TestProduct(unittest.TestCase):


    def test_discount_error(self):

        with self.assertRaises(ProductExceptionError):
            Product(name= 'Pol100', price = 10, discount= 11)

    @unittest.skip("La prueba no cumple los requerimientos")
    def test_aplicacion_cobro(self):
        n1 = 90
        n2 = 10

    @unittest.skipIf(3 == 3,"La prueba no cumple los requerimientos")
    def test_skipIf(self):
        n1 = 90
        n2 = 10

    @unittest.skipUnless(available_to_skip(),"La prueba no cumple los requerimientos")
    def test_skipUnless(self):
        n1 = 90
        n2 = 10


if __name__ == "__main__":
    unittest.main()




''' 
    assertRaises(exc, fun, *args, **kwds)       fun(*args, **kwds) raises exc

    assertRaisesRegex(exc, r, fun, *args, **kwds)       fun(*args, **kwds) raises exc and the message matches regex r

    assertWarns(warn, fun, *args, **kwds)       fun(*args, **kwds) raises warn

    assertWarnsRegex(warn, r, fun, *args, **kwds)       fun(*args, **kwds) raises warn and the message matches regex r

    assertLogs(logger, level)       The with block logs on logger with minimum level

    assertNoLogs(logger, level)     The with block does not log on  logger with minimum level 
'''

"""
    assertAlmostEqual(a, b)         round(a-b, 7) == 0

    assertNotAlmostEqual(a, b)      round(a-b, 7) != 0
    
    assertGreater(a, b)             a > b

    assertGreaterEqual(a, b)        a >= b
    
    assertLess(a, b)                a < b

    assertLessEqual(a, b)           a <= b

    assertRegex(s, r)               r.search(s)

    assertNotRegex(s, r)            not r.search(s)

    assertCountEqual(a, b)          a and b have the same elements in the same number, regardless of     
 """