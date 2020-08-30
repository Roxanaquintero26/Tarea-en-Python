import math

class calcular_area:
    def resultado(self): #Funcion que retorna el resultado del area 
        return self.area

    def area_circulo(self,radio): # Funcion para calcular el area de un circulo
        if radio >= 0:
            self.area = round((math.pi * math.pow(radio,2)),2)
        else:
            self.area = ("El radio debe de ser positivo")
      
    def area_cuadrado(self,lado): # Funcion para calcular el area de un cuadrado
        if lado >= 0:
            self.area = math.pow(lado,2)
        else:
            self.area = ("Ingrese un número positivo")
    
    def area_rectangulo(self,base,altura): # Funcion para calcular el area de un rectangulo
        if base >= 0 and altura >= 0:
            self.area = base * altura
        else:
            self.area = ("Ingrese numeros positivos para los parametros de base y altura")
    
    def area_triangulo(self,base,altura):# Funcion para calcular el area de un triangulo
        if base >= 0 and altura >= 0:
            self.area = (base * altura)/2
        else:
            self.area = ("Ingrese numeros positivos para los parametros de base y altura")

    def area_elipse(self,eje_mayor,eje_menor):# Funcion para calcular el area de una elipse
        if eje_mayor >= 0 and eje_menor >= 0:
            self.area = round((math.pi * eje_mayor * eje_menor),2)
        else:
            self.area = ("Ingrese numeros positivos para los parametros del eje mayor y el eje menor")
