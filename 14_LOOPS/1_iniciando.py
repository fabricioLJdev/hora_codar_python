# Aula 1 

contador = 1

while contador <= 5: # condição que permite loop
    
    print(f"Contador: {contador}")
    
    contador += 1 # incrementação 

"""
senha = ""

while senha != "12345": 
    senha = input("Digite a sua senha")

print("Bem-vindo ao sistema")
"""

x = 10  

while x > 10:
    print(x)
    x -= 1

"""
numero = 0

while True:
    numero = int(input("Digite um número: "))

    if numero > 0:
        print("Número positivo")
        break
"""

lista_frutas = ["limão", "maçã", "banana", "kiwi"]

for fruta in lista_frutas: # (fruta) é uma variavel temporaria que crio e dou nome especificamente para chama cada item dentro de um lista
    print(f"Fruta: {fruta}")

carros = ["Fusca", "Gol", "Ferrari", "Camaro"]

for i, carro in enumerate(carros): # (i) refere-se ao indece da lista (carro) o elementos da lista (carros) e enumerate permite o acesso aos indice da lista(carros)
    print(f"{carro} referente ao indice {i + 1}")

for numero in range(1, 6):
    print(numero)

frutas = ["limão", "maçã", "banana", "kiwi"]

for fruta in frutas:
    if "a" in fruta or "ã" in fruta:
        print(f"{fruta} tem a letra A") 
    else:
        print(f"{fruta} não contem a letra A")

# aula 3 - Range
for i in range(1, 5):
    print(f"i = a {i}")

for i in range(5): # o mesmo exemplo só omitiu o número de começo 
    print(f"i = a {i}")

for i in range(3, 16, 3):
    print(f"I = {i}")

for i in range(10, 0, -1):
    print(f"I = {i}")

nomes = ["abner", "americo", "stefani", "fabricio", "emy"]

for i in range(len(nomes)): # range ele ajudar saber o número de vezes que o loop rodou
    print(f"i = {i} {nomes[i]}")

# Aula 4 - strings, listas e dicionarios

texto = "python"

for letra in texto:
    print(f"Letra: {letra}")

dados = {
    "nome": "Abner",
    "idade": 2,
    "esta_trabalhando": False
}

for chave in dados:
    print(f"chave: {chave} - Valor {dados[chave]}")

for chave, valor in dados.items():
    print(f"{chave} - {valor}")