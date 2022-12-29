import unittest


class Example(unittest.TestCase):
    
    def test_suma_numero(self):
        numero1 = 10
        numero2 = 20
        resultado = numero1 + numero2
        # 30
        # assert resultado == 30
        self.assertEqual(resultado,30)

if __name__ == "__main__":
    unittest.main()