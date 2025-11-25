# Aula 1 - Comprensao de listas

# lista com quadrados de numeros

quadrado = [x**2 for x in range(1,10)]

numeros = [10, 20, 30, 40,50]

print(quadrado)

quadrados = [x**2 for x in numeros]

print(quadrados)


# Combinar listas 
"""
1) primeiro criei duas variaveis lista
2) criei um padrão que vai ser repetido no loop (f"{nome} tem {idade} anos")
3) chamei os elementos dentro da variaveis (nomes e idades) de "nome e idade"
4) usei in para passas a variaveis que vão ser combinadas e (zip) é para pegar as duas variaveis
"""
nomes = ["Abner", "Americo", "Stefani"]
idades = [2, 11, 22]

combinacao = [f"{nome} tem {idade}" for nome, idade in zip(nomes, idades)]

print(combinacao)

# 1) criei duas variaveis (frutas_verduras e identificaca)
# 2) criei uma compressão de lista[] onde f"{frutas_verdura} é uma {identificado}" é o padrão 
# 3) chamei os elementos de frutas_verdura e identificado e usei o zip para pegar as duas variaveis
# 4) imprimir a mensagem

frutas_verduras = ["maçã", "cenoura", "manga", "pimentão", "goiaba", "beterraba"]

identificacao = ["fruta", "verdura", "fruta", "verdura", "fruta", "verdura"]

combinando = [f"{frutas_verdura} é uma {identificado}" for frutas_verdura, identificado in zip(frutas_verduras, identificacao)]

print(combinando)

# Lista de caracteres de uma string(Palavra)

letras = [letra for letra in "Pyhton"]

letras2 = [caractere for caractere in "Lacerda"]

print(letras)

print(letras2)

# strings e listas = acesso por indice, metodo len, percorrer com for in

# Aula 2 - Ordenação de lista

numeros = [1, 10, 5, 6, 8, 2]

numeros.sort() # (sort) ordena os elementos dentro da lista, e altera a variavel original

print(numeros)

numeros.sort(reverse=True) #(reverse=True) ordena os elementos da lista de forma decrescente  

print(numeros) 

# utilizando Key

palavras = ["olá mundo testado", "teste", "testando", "mais um teste"]

palavras.sort(key=len) #passando a chave da ordenação, neste caso o len (quantidade de caracteres da string)

print(palavras)

palavras.sort(key=len, reverse=True) #ordenando com o key de forma decrescente

print(palavras)

# sorted -> não muda o dado original
numeros_2 = sorted(numeros)

print(numeros)

print(numeros_2)

# Aula 3 - Revertendo Listas

# *** Dois pontos muitos importantes caso você use o metodo reverse() ***
# 1) ele inverte o dado armazenado(variavel) e não ordena
# 2) o dado original ou variavel é alterado

estados = ["Bahia", "São Paulo", "Santa Catarina"]

estados.reverse() 

print(estados)

# caso queria presevar a variavel original usando o metodo reverse()
cidades = ["São Paulo", "Rio de Janeiro", "Salvador"]

cidades_p = list(reversed(cidades))

print(cidades)

print(cidades_p) 

nums = [1, 2, 3, 4, 5]

nums.reverse()

print(nums)

# Aula 4 - len, min, max, sum

numeros = [10, 20, 30, 40, 50]

print(len(numeros)) #(len) mostra a quantidade de elementos

print("Maior número é: ", max(numeros))

print("Menor número é: ", min(numeros))

print("A soma de todos os números é: ", sum(numeros))

# Key, trabalhar com tamanho de strings em min e max

print("Maior cidade: ", max(cidades, key=len))

print("Menor cidade: ", min(cidades, key=len))