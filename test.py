import unittest
from Programa  import calcular_area

class testAreaCirculo(unittest.TestCase):

    def test_area_del_criculo(self):
        # El area de un ciruculo con radio de 4 debe dar 50.27 redondeando a dos decimales
        area = calcular_area()
        area.area_circulo(4)
        esperamos = 50.27
        self.assertEqual(esperamos,area.resultado())
    
    def test_evalua_parametro_radio(self):
        # No se puede calcular el area del circulo si se ingresa un numero negativo
        area = calcular_area()
        area.area_circulo(-2)
        esperamos = str("El radio debe de ser positivo")
        self.assertEqual(esperamos,area.resultado())


class testAreaCuadrado(unittest.TestCase):

    def test_area_del_cuadrado(self):
        # El area del cuadrado cuyo valor sea de 4 tendra una area de 16
        area = calcular_area()
        area.area_cuadrado(4),self.assertEqual(16,area.resultado())
        
