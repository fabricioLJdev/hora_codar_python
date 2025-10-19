# ex1
'''
numero1 = int(input("Digite o n1: "))
numero2 = int(input("Digite o n2: "))

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
'''

# ex2
'''
numero_float = float(input("Digite um numero float: "))
numero_arredondado = round(numero_float, 2)

print(numero_float)
print(numero_arredondado)
'''

# ex3
'''
numero_int = int(input("Digite um numero inteiro: "))
numero_convertido_float = float(numero_int)

numero_float = float(input("Digite um numero float: "))
numero_convertido_int = int(numero_float)

print(numero_convertido_float, numero_convertido_int)
'''

# ex4
import math
'''
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

print(raiz1, raiz2)
'''

# ex5
raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio**2)

print(area)