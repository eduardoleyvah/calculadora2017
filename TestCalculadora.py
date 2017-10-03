import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.operaciones = Calculadora()

	def test_sumar_2_mas_2_igual_4(self):
		self.operaciones.suma(2, 2)
		self.assertEquals(self.operaciones.obtener_resultado(),4)

	def test_sumar_1_mas_12_igual_13(self):
		self.operaciones.suma(1, 12)
		self.assertEquals(self.operaciones.obtener_resultado(),13)

	def test_sumar_3_mas_3_igual_6(self):
		self.operaciones.suma(3, 3)
		self.assertEquals(self.operaciones.obtener_resultado(),6)

	def test_sumar_menos1_mas_2_igual_1(self):
		self.operaciones.suma(-1, 2)
		self.assertEquals(self.operaciones.obtener_resultado(),1)

	def test_sumas_l_mas_2_igual_dato_invalido(self):
		self.operaciones.suma('L', 2)
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_valor_de_inicio_es_igual_a_cero(self):
		self.operaciones.suma(0,2)
		self.assertEquals(self.operaciones.obtener_resultado(), 'No se aceptan ceros')

	def test_no_se_aceptan_numeros_mayores_a_diezmil(self):
		self.operaciones.suma(5,10001)
		self.assertEquals(self.operaciones.obtener_resultado(),'No se aceptan numeros mayores a 10000')

	def test_restar_5_menos_4_igual_1(self):
		self.operaciones.resta(5,4)
		self.assertEquals(self.operaciones.obtener_resultado(),1)

	def test_restar_3_menos_3_igual_0(self):
		self.operaciones.resta(3,3)
		self.assertEquals(self.operaciones.obtener_resultado(),0)

	def test_restar_segundo_numero_mayor(self):
		self.operaciones.resta(2,5)
		self.assertEquals(self.operaciones.obtener_resultado(),'El segundo numero no debe ser mayor al primero')

	def test_restar_8_menos_N_datos_invalidos(self):
		self.operaciones.resta(8,'N')
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_multiplicar_3_por_2_igual_6(self):
		self.operaciones.multiplicacion(3,2)
		self.assertEquals(self.operaciones.obtener_resultado(),6)

	def test_multiplicar_menos2_por_2_igual_menos4(self):
		self.operaciones.multiplicacion(-2,2)
		self.assertEquals(self.operaciones.obtener_resultado(),-4)

	def test_multiplicar_menos2_por_menos2_igual_4(self):
		self.operaciones.multiplicacion(-2,-2)
		self.assertEquals(self.operaciones.obtener_resultado(),4)

	def test_multiplicar_0_por_5_no_se_acepta(self):
		self.operaciones.multiplicacion(0,5)
		self.assertEquals(self.operaciones.obtener_resultado(),'No se aceptan ceros')

	def test_multiplicar_R_por_7_datos_incorrectos(self):
		self.operaciones.multiplicacion('R',7)
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_division_4_entre_2_igual_2(self):
		self.operaciones.division(4,2)
		self.assertEquals(self.operaciones.obtener_resultado(),2)

	def test_division_1_entre_10_igual_0(self):
		self.operaciones.division(1,10)
		self.assertEquals(self.operaciones.obtener_resultado(),0)

	def test_divison_H_entre_1_datos_incorrecots(self):
		self.operaciones.division('H',1)
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_division_1_entre_0_indeterminacion(self):
		self.operaciones.division(1,0)
		self.assertEquals(self.operaciones.obtener_resultado(),'Indeterminacion')

	def test_division_1_entre_menos1_igual_menos1(self):
		self.operaciones.division(1,-1)
		self.assertEquals(self.operaciones.obtener_resultado(),-1)

	def test_raiz_de_5_igual_2punto2(self):
		self.operaciones.raiz(5,0)
		self.assertEquals(self.operaciones.obtener_resultado(),2.2)

	def test_raiz_de_0_igual_0punto0(self):
		self.operaciones.raiz(0,0)
		self.assertEquals(self.operaciones.obtener_resultado(),0.0)

	def test_raiz_de_menos1_no_se_pueden_negativos(self):
		self.operaciones.raiz(-1,0)
		self.assertEquals(self.operaciones.obtener_resultado(),'No se puede sacar raiz de un numero negativo')

	def test_raiz_de_L_datos_incorrectos(self):
		self.operaciones.raiz('L',0)
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_potencia_de_5_al_cuadrado_igual_25(self):
		self.operaciones.potencia(5,2)
		self.assertEquals(self.operaciones.obtener_resultado(),25)

	def test_potencia_de_3_a_la_j_datos_incorrectos(self):
		self.operaciones.potencia(3,'j')
		self.assertEquals(self.operaciones.obtener_resultado(),'datos incorrectos')

	def test_potencia_de_2_a_la_menos2_no_se_pueden_negativos(self):
		self.operaciones.potencia(2,-2)
		self.assertEquals(self.operaciones.obtener_resultado(),'No se aceptan negativos')

	def test_potencia_de_3_a_la_11_no_se_pueden_mayores_a_10(self):
		self.operaciones.potencia(3,11)
		self.assertEquals(self.operaciones.obtener_resultado(),'No se aceptan exponentes mayores a 10')

	def test_edad_menor_a_0_no_existes(self):
		self.operaciones.edad(-1)
		self.assertEquals(self.operaciones.obtener_resultado(),'No existes')	

	def test_edad_menor_a_13_eres_ninio(self):
		self.operaciones.edad(10)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres ninio')

	def test_edad_menor_a_18_eres_adolescente(self):
		self.operaciones.edad(15)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adolescente')

	def test_edad_menor_a_65_eres_adulto(self):
		self.operaciones.edad(33)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adulto')	

	def test_edad_menor_a_120_eres_adulto_mayor(self):
		self.operaciones.edad(105)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres adulto mayor')	

	def test_edad_mayor_a_120_eres_mummra(self):
		self.operaciones.edad(200)
		self.assertEquals(self.operaciones.obtener_resultado(),'Eres Mumm-Ra')			

if __name__ == '__main__':
	unittest.main()

"""
>>> suma(2,2)
4

>>> suma(3,3)
6

>>> suma(-1,2)
1

>>> suma('L',2)
'datos incorrectos'

>>> suma(0,2)
'No se aceptan ceros'

>>> suma(5,10001)
'No se aceptan numeros mayores a 10000'

>>> resta(5,4)
1

>>> resta(3,3)
0

>>> resta(2,5)
'El segundo numero no debe ser mayor al primero'

>>> resta(8,'N')
'datos incorrectos'

>>> multiplicacion(3,2)
6

>>> multiplicacion(-2,2)
-4

>>> multiplicacion(-2,-2)
4

>>> multiplicacion(0,5)
'No se aceptan ceros'

>>> multiplicacion('R',7)
'datos incorrectos'

>>> division(4,2)
2

>>> division(1,10)
0

>>> division('H',1)
'datos incorrectos'

>>> division(1,0)
'Indeterminacion'

>>> division(1,-1)
-1

>>> raiz(5,0)
2.2

>>> raiz(0,0)
0.0

>>> raiz(-1,0)
'No se puede sacar raiz de un numero negativo'

>>> raiz('L',0)
'datos incorrectos'

>>> potencia(5,2)
25

>>> potencia(3,'j')
'datos incorrectos'

>>> potencia(2,-2)
'No se aceptan negativos'

>>> potencia(3,11)
'No se aceptan exponentes mayores a 10'

>>> edad(-1)
'No existes'

>>> edad(10)
'Eres ninio'

>>> edad(15)
'Eres adolescente'

>>> edad(33)
'Eres adulto'

>>> edad(105)
'Eres adulto mayor'

>>> edad(200)
'Eres Mumm-Ra'
"""