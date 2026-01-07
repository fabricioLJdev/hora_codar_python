# Aula 1 - break

for numero in range(1, 50):
    print("Numero: ", numero)

    if numero % 7 == 0:
        print("Encontramos o numero ", numero)

        break

"""
while True:
    comando = input("Digite 'sair' para encerrar: ")
    
    if comando.lower() == 'sair': #use "lower" para dar um precisão na hora que o usuario for digitar
        
        print("Encerrando o programa...")
        break

    print(comando)
"""

frutas = ["laranja", "maçã", "manga", "uva", "goiaba"]

for fruta in frutas:
    if fruta == "uva":
        print("Encontramos a uva...")
        break
    print(fruta)

# Aula 2 - continue
numeros = [1, -3, 4, -5, 9, -2]


for numero in numeros:
    if numero < 0:
        continue  #(continue) ira pular a execução determinada no if
    print("O numero é: ", numero)

texto = "Python3.1234"

for letra in texto:
    if not letra.isalpha(): # se não for isalpha() ou letra
        continue
    print("Letra: ", letra)

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)

print("Aula 3")
# break encerra o loop
# continue pula para a prox. execução 

# Aula 3 - combinacao de break e continue

for numero in range(1, 20):
    if numero % 2 != 0:
        continue

    elif numero % 5 == 0:
        print(f"Primero numero divisivel por 5: {numero}")
        break

numeros = [1, -3, 4, -5, 9, -2]

for numero in numeros:
    if numero < 0:
        continue

    elif numero > 5:
        print("Numero maior que o previsto, parando o loop...")
        break
