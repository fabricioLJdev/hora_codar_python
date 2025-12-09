# Aula 1 - metodos uteis
frutas = ["maçã", "banana", "Laranja", "Melancia", "morango", "banana"]

# metodo "count()" mostra quantas vezes um elemento está em uma lista
print(frutas.count("banana"))
print(frutas.count("maçã"))
print(frutas.count("kiwi")) # se colocar uma elemnto no metodo count que não exista, não quebra o código

# o metodo "index()", é usando para saber em que indice está um elemento dentro de uma lista
print(frutas.index("Melancia"))
print(frutas.index("banana"))
# el. n existe = error=> print(frutas.index("kiwi"))

# o metodo "clear()" deleta todos elementos da lista e já era
teste = frutas.clear()

print(teste)

print(frutas)

# Aula 2 - listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)

# acessando a 2 lista
print(matriz[1])

# primeiro index = lista, segundo index = el.
print(matriz[2][1])

# adicionando uma novo sublista
nova_linha = [10, 11, 12]

matriz.append(nova_linha)

print(matriz)

# Aula 3 - continuando listas aninhadas
print(matriz[2][0]) 

matriz[0][1] = 99

print(matriz)

matriz.pop(1) # excluindo a segunda sublista

print(matriz)

matriz[0].append(8) # adicionando um el. na primeira sublista

print(matriz)

# acessando sublistas, podemos usar os metodos de lista normalmente

matriz.append([11, 12, 13]) # adicionando um nova sublista

print(matriz)

matriz[3].pop(1) # exluindo um el. especifico de uma sublista

print(matriz)

# Aula 4 - iterando sobre listas
lista_nova = [1, 2, 3, 4, 5]

# for in
for numero in lista_nova:
    print("O númreo da vez é: ", numero)

# i => pode ser chamado de qualquer coisa (i, m, j, n)
for i, linha in enumerate(matriz):
    print(f"Linha {i + 1}: {linha}")

for linha in matriz:
    print(linha)
    for numero in linha:
        print("Valor: ", numero)

i = 0
while i < len(lista_nova):
    print("Número: ", lista_nova[i])
    i += 1