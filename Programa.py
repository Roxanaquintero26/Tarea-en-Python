import math

class calcular_area:
    def resultado(self):
        return self.area

    def area_circulo(self,radio):
        if radio >= 0:
            self.area = round((math.pi * math.pow(radio,2)),2)
        else:
            self.area = ("El radio debe de ser positivo")
      
    def area_cuadrado(self,lado):
        if lado >= 0:
            self.area = math.pow(lado,2)
        else:
            self.area = ("Ingrese un número positivo")