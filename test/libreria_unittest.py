import unittest


class Example(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Se ejecuta antes de las Pruebas")

    @classmethod
    def tearDownClass(cls):
        print("Se ejecuta despues de las pruebas")

    def setUp(self):
        print("Ejecutando el setup")


    def tearDown(self):
        print("Ejecutando el teardown")
    
    def test_suma_numero(self):
        numero1 = 10
        numero2 = 20
        resultado = numero1 + numero2
        # 30
        # assert resultado == 30
        self.assertEqual(resultado,30)


    def test_resta_numero(self):
        numero1 = 20
        numero2 = 10
        resultado = numero1 - numero2
        self.assertEqual(resultado,10)

if __name__ == "__main__":
    unittest.main()

# Metodos Assert

''' 
    assertEqual(a, b)   a == b
    assertNotEqual(a, b)    a != b
    assertTrue(x)   bool(x) is True
    assertFalse(x)  bool(x) is False
    assertIs(a, b)  a is b
    assertIsNot(a, b)   a is not b
    assertIsNone(x) x is None
    assertIsNotNone(x)  x is not None
    assertIn(a, b)  a in b
    assertNotIn(a, b)   a not in b
    assertIsInstance(a, b)  isinstance(a, b)
    assertNotIsInstance(a, b)   not isinstance(a, b) 
'''