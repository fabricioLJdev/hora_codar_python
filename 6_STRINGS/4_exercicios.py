"""
# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie uma string com a frase "Python é incrível", substitua a palavra "incrível"
# por "fantástico" e exiba o resultado.
# Descrição: O programa deve criar uma string, usar o método replace() para substituir uma
# palavra específica e exibir o texto atualizado.

frase = "Python é incrível"
frase_alterada = frase.replace("incrível", "fantástico")

print(frase_alterada)
"""
"""
# Exercício 2:
# Enunciado: Escreva um programa que receba o nome completo de um usuário, divida o nome
# em partes e exiba o primeiro e o último nome separadamente.
# Descrição: O programa deve usar o método split() para dividir a string do nome em uma lista
# de palavras e acessar o primeiro e o último elementos da lista.

nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()

primeiro_nome = partes[0]
segundo_nome = partes[1]

print("Primeiro nome é:",primeiro_nome)
print("Segundo nome é:",segundo_nome)
"""
"""
# Exercício 3:
# Enunciado: Desenvolva um programa que solicite uma lista de itens separados por vírgulas
# e os exiba em uma única string, com os itens separados por ponto e vírgula.
# Descrição: O programa deve receber uma entrada de texto, usar o método split() para criar
# uma lista e depois o método join() para concatenar os itens com o delimitador ";".

itens = input("Digite uma lista com três separados por vírgula: ")
lista = itens.split(",")

resultado = ";".join(lista)

print(resultado)
"""

"""
# Exercício 4:
# Enunciado: Crie uma string multilinha com uma mensagem de boas-vindas que inclua variáveis
# como o nome do usuário e a data atual, formatada com f-strings.
# Descrição: O programa deve usar uma string multilinha com aspas triplas e incluir variáveis
# formatadas dinamicamente com f-strings para exibir uma mensagem personalizada.

from datetime import date

nome_usuario = input("Digite seu nome completo: ")
mes = date.today().strftime("%d/%m/%Y")

mensagem = f'''
    Bem vindo {nome_usuario}
    Hoje é {mes}
'''

print(mensagem)
"""

"""
# Exercício 5:
# Enunciado: Escreva um programa que receba uma string, conte o número de vogais na string
# e exiba o total de vogais encontradas.
# Descrição: O programa deve iterar pela string, verificar se cada caractere é uma vogal e
# manter um contador que será exibido ao final.

texto = input("Digite seu nome completo ou uma frase: ")

vogais = "aeiouAEIOU"

contador = sum(1 for char in texto if char in vogais) #para cada caracteres no texto se caracteres ester dentro de vogais some 1

print("Total de vogais é: ", contador)
"""