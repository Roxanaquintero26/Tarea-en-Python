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
    
    def area_rectangulo(self,base,altura):
        if base >= 0 and altura >= 0:
            self.area = base * altura
        else:
            self.area = ("Ingrese numeros positivos para los parametros de base y altura")
    