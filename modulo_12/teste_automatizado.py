import unittest

class calculadora :
    def subtrair(self, num1, num2) :
        return num1 - num2

    def somar(self, num1, num2) :
        return num1 + num2

    def dividir(self, num1, num2) :
        if num2 == 0 :
            raise ValueError ( "Erro! Não é permitido divisão por zero" )
        return num1 / num2

class Testcalculadora ( unittest.TestCase ) :
    def test_negativos(self) :
        self.assertEqual ( calculadora ().subtrair ( 5, 2 ), 3 )

    def test_positivos(self) :
        self.assertEqual ( calculadora ().somar ( 5, 8 ), 13 )

    def test_divisao_zero(self):
         with self.assertRaises(ValueError):
              calculadora().dividir(13, 0)

if __name__ == '__main__' :
    unittest.main ()