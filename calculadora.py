import math

# Luis Eduardo Leyva Herrera
# Matricula: 34150284

class Calculadora():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
    	if type(num1) is str or type(num2) is str:
    		self.resultado = 'datos incorrectos'
    	elif num1 == 0 or num2 == 0:
    		self.resultado =  'No se aceptan ceros'
    	elif num1 > 10000 or num2 > 10000:
    		self.resultado =  'No se aceptan numeros mayores a 10000'
        else:
            self.resultado = num1 + num2
    	
    def resta(self, num1, num2):
        if type(num1) is str or type(num2) is str:
    		self.resultado ='datos incorrectos'
        elif num2 > num1:
            self.resultado = 'El segundo numero no debe ser mayor al primero'
        elif num1 == 0 or num2 == 0:
    		self.resultado = 'No se aceptan ceros'
        else:
            self.resultado = num1 - num2

    def multiplicacion(self, num1, num2):
        if type(num1) is str or type(num2) is str:
    		self.resultado = 'datos incorrectos'
        elif num1 == 0 or num2 == 0:
    		self.resultado = 'No se aceptan ceros'
        else:
            self.resultado = num1 * num2

    def division(self, num1, num2):
        if type(num1) is str or type(num2) is str:
    		self.resultado = 'datos incorrectos'
        elif num2 == 0:
            self.resultado = 'Indeterminacion'
        else:
            self.resultado = num1 / num2

    def raiz(self, num1, num2):
        if type(num1) is str:
    		self.resultado = 'datos incorrectos'
        elif num1 < 0:
            self.resultado = 'No se puede sacar raiz de un numero negativo'
        else:
            self.resultado = round((math.sqrt(num1)+num2),1)

    def potencia(self, num1, num2):
        if type(num1) is str or type(num2) is str:
    		self.resultado = 'datos incorrectos'
        elif num2 < 0:
            self.resultado = 'No se aceptan negativos'
        elif num2 > 10:
            self.resultado = 'No se aceptan exponentes mayores a 10'
        else:
            self.resultado = pow(num1,num2)

    def edad(self,num1):
        if num1 < 0:
            self.resultado = 'No existes'
        elif num1 > 0 and num1 < 13:
            self.resultado = 'Eres ninio'
        elif num1 > 13 and num1 < 18:
            self.resultado = 'Eres adolescente'
        elif num1 > 18 and num1 < 65:
            self.resultado = 'Eres adulto'
        elif num1 > 65 and num1 < 120:
            self.resultado = 'Eres adulto mayor'
        else:
            self.resultado = 'Eres Mumm-Ra'


