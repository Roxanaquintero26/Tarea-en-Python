import unittest
from Programa  import calcular_area

class testAreaCirculo(unittest.TestCase):
    
    def test_area_del_criculo(self):
        # El area de un ciruculo con radio de 4 debe dar 50.27 redondeando a dos decimales
        area = calcular_area()
        area.area_circulo(4)
        esperamos = 50.27
        self.assertEqual(esperamos,area.resultado())
    


