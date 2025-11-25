# Exercício 1:
# Enunciado: Crie uma lista com os números de 1 a 10. Use append() para adicionar o número 11
# e insert() para adicionar o número 0 no início da lista. Exiba a lista resultante.
# Descrição: O programa deve criar uma lista inicial, usar métodos para adicionar elementos no
# início e no final, e exibir a lista modificada.

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_numeros.append(11)
lista_de_numeros.insert(0, 0)

print(lista_de_numeros)

# Exercício 2:
# Enunciado: Escreva um programa que receba uma lista de nomes e conte quantas vezes um nome
# específico aparece na lista usando count().
# Descrição: O programa deve receber uma lista de nomes e um nome de busca, calcular quantas
# vezes o nome aparece na lista usando count() e exibir o resultado.

nomes = ["Abner", "Stefani", "Fabricio", "Abner"]

nome_busca = "Abner"

quantidade = nomes.count(nome_busca)

print(quantidade)

# Exercício 3:
# Enunciado: Desenvolva um programa que organize uma lista de números em ordem crescente e
# depois inverta essa lista. Exiba os resultados em ambas as etapas.
# Descrição: O programa deve usar sort() para ordenar a lista e reverse() para inverter a
# ordem, exibindo os resultados após cada operação.

nums = [1, 10, 3, 5, 2, 4, 6, 8, 7, 9]

print("Os numeros são: ", nums)

nums.sort()

print("Em ordem ", nums)

nums.sort(reverse=True)

print("Em ordem reversa: ", nums)

# Exercício 4:
# Enunciado: Crie uma lista aninhada que representa uma matriz 3x3. Acesse e modifique o valor
# do elemento da segunda linha, terceira coluna. Exiba a matriz antes e depois da modificação.
# Descrição: O programa deve criar uma lista aninhada para representar a matriz, modificar
# um valor específico usando índices e exibir as duas versões da matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

novo_valor = 10

matriz[1][2]  = novo_valor

print(matriz)

# Exercício 5:
# Enunciado: Escreva um programa que receba uma lista de números e exiba o menor valor, o
# maior valor, o número total de elementos e a soma de todos os valores.
# Descrição: O programa deve usar as funções len(), min(), max() e sum() para calcular os
# resultados e exibi-los de forma organizada.

valores = [1000, 10, 100, 150, 250]

print("Exibindo lista de numeros", valores)
print(min(valores),"é o valor menor")
print(max(valores),"é o valor maior")
print(len(valores),"é a quantidade de numeros")
print(sum(valores),"é a soma de todos os números")