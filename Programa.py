import math

class calcular_area:
    def resultado(self):
        return self.area

    def area_circulo(self,radio):
        self.area = round((math.pi * math.pow(radio,2)),2)
       
        