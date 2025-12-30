# Aula 1 - if
if True:
    print("Deu certo")

numero = 6

if numero % 2 == 0:
    print("O número é par")

valor = 10
valor2 = 20

if valor < valor2:
    print("O valor 1 é menor que o valor 2")

lista = [1, 2, 3, 4]

numero = 2

if numero in lista:
    print("O número 2 está na lista")

# Aula 2 - else
numero = 11

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")

idade = 27

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é MENOR de idade")

"""
valor = int(input("Digite um número positivo: "))

if valor > 0:
    print(f"O valor {valor} é positivo!")
else:
    print("Você digitou um número negativo!")
"""

# Aula 3 - Elif
idade = 11

if idade < 13:
    print("Você é uma criança")
elif idade < 18:
    print("Você é um adolescente")
else:
    print("Você é adulto")

nota = 6.9

if nota >= 9:
    print("Você foi muito bem!")
elif nota >= 8:
    print("Você foi bem")
elif nota >= 7:
    print("Você fico na média")
elif nota >= 6:
    print("Você está de recuperação")
else:
    print("Você foi muito mal, faça aulas de reforço")

# podemos ter só if
# não podemos ter só else
# podemos ter if e elif, sem else
# podemos ter quantos elif's quisermos
# nem if e nem elif, requerem false
