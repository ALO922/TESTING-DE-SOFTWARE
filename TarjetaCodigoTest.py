import unittest
from TarjetaCodigo import TarjetaCodigo

class TestTarjetaCodigo(unittest.TestCase):
    def setUp(self):
        self.tarjeta = TarjetaCodigo()
        
    def test_numeroTarjeta(self):
        # Casos de prueba para numeroTarjeta
        self.assertTrue(self.tarjeta.numeroTarjeta("1234567890123456"))  # Número válido
        self.assertFalse(self.tarjeta.numeroTarjeta("1234"))  # Número con longitud incorrecta
        self.assertFalse(self.tarjeta.numeroTarjeta("123456789012345a"))  # Número con caracteres no numéricos
        self.assertTrue(self.tarjeta.numeroTarjeta("9876543210987654"))  # Otro número válido

    def test_fechaTarjeta(self):
        # Casos de prueba para fechaTarjeta
        self.assertTrue(self.tarjeta.fechaTarjeta("12/25"))  # Fecha válida
        self.assertFalse(self.tarjeta.fechaTarjeta("13/25"))  # Mes fuera de rango
        self.assertFalse(self.tarjeta.fechaTarjeta("12/20"))  # Fecha anterior a 2023
        self.assertTrue(self.tarjeta.fechaTarjeta("05/24"))  # Otra fecha válida

    def test_codigoTarjeta(self):
        # Casos de prueba para codigoTarjeta
        self.assertTrue(self.tarjeta.codigoTarjeta("123"))  # Código válido
        self.assertFalse(self.tarjeta.codigoTarjeta("12"))  # Código con longitud incorrecta
        self.assertFalse(self.tarjeta.codigoTarjeta("12a"))  # Código con caracteres no numéricos
        self.assertTrue(self.tarjeta.codigoTarjeta("999"))  # Otro código válido

    def test_verificarSaldo(self):
        # Casos de prueba para verificarSaldo
        self.assertTrue(self.tarjeta.verificarSaldo("100", "500"))  # Saldo suficiente
        self.assertFalse(self.tarjeta.verificarSaldo("600", "500"))  # Valor a pagar mayor que saldo
        self.assertFalse(self.tarjeta.verificarSaldo("abc", "500"))  # Valor a pagar no numérico
        self.assertFalse(self.tarjeta.verificarSaldo("100", "abc"))  # Saldo no numérico

if __name__ == '__main__':
    unittest.main()