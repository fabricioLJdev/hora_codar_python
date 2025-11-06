# Aula 1 = Métodos de strings

# formatação
texto = 'python é muito leGal'

print(texto.upper())
print(texto.lower())
print(texto.capitalize())

# remoção de espaço
espacos = " teste aqui em Python           "

espacos_limpos = espacos.strip()

print(espacos)
print(espacos_limpos)

# substituicao de caracteres
print(espacos.replace("Python", "PHP"))

dados = "nome,telefone,endereco"

dados_separado = dados.split(',')

print(dados_separado)

# Aula 2 split
frase = "Python é muito divertido"

lista_frase = frase.split() # cada palavra dentro da string vira elementos

print(lista_frase)

# indices de lista tb comecam com 0 (primeiro elemento)
print(lista_frase[1])

string_caracteres = "teste-tastando-testou"

print(string_caracteres.split("-"))

# maxsplit = funciona por numero de indices
print(frase.split(" ", 1))

# Aulo 3 join
palavras = ["Python", "é", "incrivel"]

print(" ".join(palavras))

print(",".join(palavras))

numeros = [1, 2, 3]

# map -> percorrer uma lista, e modificar eles

print(" ".join(map(str, numeros)))

# Aula 4 Replace
texto = "Python é otimo"

print(texto.replace("otimo", "perfeito"))

palavras = "maçã, banana, maçã, manga, maçã"

# terceiro arg: qtd de substituições
print(palavras.replace("maçã", "teste", 2))

# limpar caracteres
texto = "sei lá @ teste !"

print(texto.replace("@", "").replace("!", ""))