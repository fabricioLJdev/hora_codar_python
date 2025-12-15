# AUla 1 - Op. de identidade
# (==) compara os valores
# (is) Retorna True se ambas as variáveis apontam para o mesmo objeto
# (is not) retorna true se ambas variáveis pertecem a objetos diferentes


x = None

print(x is None)
print(x == None)
print(x is not None) # inverte o resultado booleano 

a = 10
b = 10

print(a is b)
print(a == b)

lista = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista

print(lista is lista2) # Retorna False, apesar de terem o mesmo conteúdo, são objetos diferentes

print(lista is not lista2) # Retorna True, as duas variaveis são de objetos diferentes

print(lista3 is lista) # Retorna True, lista3 referencia o mesmo objeto lista

s1 = "Python"
s2 = "Python"

print(s1 is s2)
print(s1 == s2)

d = {}
d2 = {}

print(d is d2)

t = ()
t2 = ()

print(t is t2) 

# Aula 2 - Op. de associação
frutas = ["Maçã", "Banana", "Laranja"]

print("Maçã" in frutas) # in, verifica se um valor está em uma variável lista
print("Abacate" not in frutas) # not in, verifica se um valor não está em uma variável lista 

frase = "Python é muito legal"

print("Python" in frase) # verificando se a palavra está presente na variavel

print("Java" in frase)

print("Java" not in frase) # True -> a string não está presente na variável

# dicionarios = lista de dados com chave e valor
pessoa = {"nome": "Abner", "idade": 2}

# verificando se a chave está presente no diciónario
print("nome" in pessoa)

# verificando se o valor está presente no diciónario
print("Ste" in pessoa.values())

# tupla = lista imutavel
numeros = (1, 2, 3, 4, 5)

# verificando se o número está na variável
print(1 in numeros)
print(10 in numeros)

# Aula 3 - operadores com condições e calculos
'''
entrada = input("Digite um número: ")

numeros = [1, 2, 3, 4, 5]

if int(entrada) in numeros:
    print("Você acertou!")
'''

idade = input("Digite sua idade: ")
renda = input("Digite sua renda: ")

if int(idade) < 30 and int(renda) > 5000:
    print("Vocês está ganhando bem!")
else:
    print("Você ainda não ganha bem!")

frase = "PHP e Python são linguagem de programação"

if "PHP" in frase and "Python" in frase:
    print("O texto fala sobre Python e PHP")