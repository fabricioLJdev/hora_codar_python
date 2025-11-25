# Aula 1
lista_vazia = [] #criando uma lista vazia

print(lista_vazia)

print(len(lista_vazia)) # a função "len" da o comprimento da lista

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1)

print(len(lista1))

lista_concatenada = lista1 + lista2 #concatenar = juntar 

print(lista_concatenada)

lista_repetida = lista2 * 3 #os elementos ira se repetir três vezes dentro de uma lista 

print(lista_repetida)

# Verificando se um elemento está dentro de uma lista (in e not in)

print(2 in lista1)
print(10 not in lista2)
print(3 in lista2)
print(9 not in lista1)

# modificar elementos ou valores da lista

lista1[0] = 10

print(lista1)

# imprimindo um elemento especifico de uma lista
print(lista2[2]) #indice na lista começa de 0

# cuidado ao imprimir um elemento que não esteja na lista pode quebrar o programa

# error => print(lista2[10])

# Aula 2 - Adicionando elementos

animais = ["cachorro", "gato"]

animais.append("pássaro") #a função append adiciona o elemento no final da lista

print(animais)

# a função insert, podi escolher em que indice você quer adicionar um elemnto

animais.insert(1, "coelho") # (1) é o indice e ("coelhor") é o valor para ser adicionado 

print(animais)

# Adicionando elementos a uma lista vazia

numeros = []

numeros.append(0)
numeros.append(2)
numeros.insert(1, 1)

print(numeros)

# Aula 3 - remoção de itens
print(animais)

animais.remove("gato")

print(animais)

primeiro_el = animais.pop(0) # o metodo pop alem de permiti excluir um elemento, permite que você resgate o elemento exluído

print(animais)
print(primeiro_el)

animais.pop() # usar o elemento pop sem o indice, exlui o ultimo elemento

print(animais)

# indice e el. que não existe, gera erro
# erro => animais.pop("algoqnaoexiste")
# erro => animais.pop(15)