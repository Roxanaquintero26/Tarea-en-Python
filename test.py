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
        
    def test_evalua_parametro_lado(self):
        # No se puede calcular el area de un cuadrado si se ingresa un numero negativo
        area = calcular_area()
        area.area_cuadrado(-7)
        esperamos = str("Ingrese un número positivo")
        self.assertEqual(esperamos,area.resultado())

class testAreaRectangulo(unittest.TestCase):

    def test_area_del_rectangulo(self):
        # El area de unrectangulo con base de 4 y una altura de 5 debe de ser de 20
        area = calcular_area()
        area.area_rectangulo(4,5)
        self.assertEqual(20,area.resultado())

    def test_evalua_parametro_base_y_altura(self):
        # No se puede calcular el area de un rectangulo si se ingresan un numeros negativos
        area = calcular_area()
        area.area_rectangulo(-8,7)
        esperamos = str("Ingrese numeros positivos para los parametros de base y altura")
        self.assertEqual(esperamos,area.resultado())

class testAreaTriangulo(unittest.TestCase):
    def test_area_del_triangulo(self):
        # El area de un triangulo con base de 3.5 y 
        area = calcular_area()
        area.area_triangulo(8,5)
        self.assertEqual(20,area.resultado())

    def test_evalua_parametro_base_y_altura_del_triangulo(self):
        # No se puede calcular el area de un triangulo si se ingresan un numeros negativos
        area = calcular_area()
        area.area_triangulo(2,-7)
        esperamos = str("Ingrese numeros positivos para los parametros de base y altura")
        self.assertEqual(esperamos,area.resultado())