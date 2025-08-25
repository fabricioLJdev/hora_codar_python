# # ENUNCIADOS E DESCRIÇÕES

# # Exercício 1:
# # Enunciado: Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.
# # Descrição: O programa deve utilizar a função print() para exibir a mensagem
# # "Olá, Mundo!" no console. Este exercício reforça o uso básico da função
# # print() e a estrutura simples de um programa Python.

# # Exercício 2:
# # Enunciado: Escreva um programa que solicite o nome do usuário e exiba uma
# # saudação personalizada.
# # Descrição: O programa deve usar a função input() para receber o nome do
# # usuário e armazená-lo em uma variável. Em seguida, deve exibir uma mensagem
# # de saudação que inclua o nome fornecido, utilizando a função print().

# # Exercício 3:
# # Enunciado: Desenvolva um programa que demonstra o uso correto da indentação
# # em uma estrutura condicional.
# # Descrição: O programa deve solicitar um número ao usuário e verificar se ele
# # é positivo, negativo ou zero. Utilize estruturas condicionais com a
# # indentação adequada para determinar e exibir o resultado.

# # Exercício 4:
# # Enunciado: Crie um programa que solicita dois números ao usuário e exibe a
# # soma deles.
# # Descrição: O programa deve utilizar a função input() para receber dois
# # números, converter as entradas para o tipo numérico apropriado float(), calcular a
# # soma e exibir o resultado utilizando print().

# # Exercício 5:
# # Enunciado: Escreva um programa que calcula a idade do usuário com base no ano
# # de nascimento fornecido.
# # Descrição: O programa deve solicitar o ano de nascimento do usuário, converter
# # a entrada para inteiro, calcular a idade atual considerando o ano atual e
# # exibir a idade utilizando print(). Utilize comentários para explicar cada
# # etapa do código.

# EX1
print("Olá, Mundo!")

# EX2 
nome = input("Olá, tudo bem? Qual é o seu nome?")

print(f"Bem vindo {nome} a uns dos meus primeiros projetos em python!")

# EX3
if 10 > 5:
    print("Realmente 10 é maior que 5")

# EX4
primeiro_numero = input("digíte o primeiro número:")
segundo_numero = input("digíte o segundo número:")

# *** MUITO IMPORTANTE!! LEMBRE-SE, QUE A FUNÇÃO INPUT EM PYTHON SEMPRE RECEBE O VALOR EM STRING
somar = float(primeiro_numero) + float(segundo_numero)

print("O resultado é:", somar)

# EX5
ano_de_nascimento = input("Vamos descobri a sua idade? Qual seu ano de nascimento?") #pegando dados do usuario

ano_atual = 2025 #ano de referência

descobrindo_idade = ano_atual - int(ano_de_nascimento) #subtraindo e convertendo 

print(f"Você tem {descobrindo_idade} anos") #exibindo o resultado 
