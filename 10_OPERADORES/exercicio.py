# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Escreva um programa que solicite dois números ao usuário e use operadores de comparação
# para verificar se o primeiro número é maior, menor ou igual ao segundo. Exiba os resultados.
# Descrição: O programa deve capturar dois números do usuário, realizar as comparações com operadores
# (<, >, ==) e exibir mensagens indicando a relação entre os números.

# Exercício 2:
# Enunciado: Desenvolva um programa que receba três números e determine se o primeiro é menor que o
# segundo e maior que o terceiro utilizando operadores combinados.
# Descrição: O programa deve capturar três números e verificar a relação combinada entre eles usando
# operadores (<, >) em uma única expressão.

# Exercício 3:
# Enunciado: Crie um programa que receba a idade de uma pessoa e verifique se ela está apta a votar
# (idade maior ou igual a 16) ou a dirigir (idade maior ou igual a 18) usando operadores lógicos.
# Descrição: O programa deve capturar a idade do usuário, aplicar condições com operadores (and, or)
# e exibir as mensagens correspondentes às permissões.

# Exercício 4:
# Enunciado: Escreva um programa que compare duas listas para verificar se elas ocupam o mesmo espaço
# na memória usando operadores de identidade (is) e verifique se um elemento específico está presente
# em ambas usando operadores de associação (in).
# Descrição: O programa deve criar duas listas, realizar a comparação de identidade com (is) e verificar
# a presença de um elemento em ambas as listas usando (in).

# Exercício 5:
# Enunciado: Implemente um sistema de validação de login que verifica se o nome de usuário e a senha
# inseridos estão corretos, combinando operadores lógicos, de associação e de comparação.
# Descrição: O programa deve verificar se as credenciais inseridas pelo usuário coincidem com as
# credenciais armazenadas e exibir mensagens de sucesso ou e


'''
# Exercício 1:
# Enunciado: Escreva um programa que solicite dois números ao usuário e use operadores de comparação
# para verificar se o primeiro número é maior, menor ou igual ao segundo. Exiba os resultados.
# Descrição: O programa deve capturar dois números do usuário, realizar as comparações com operadores
# (<, >, ==) e exibir mensagens indicando a relação entre os números.


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}!")
elif numero1 < numero2:
    print(f"{numero1} é menor que {numero2}!")
else:
    print("Os números são iguais.")
'''

'''
# Exercício 2:
# Enunciado: Desenvolva um programa que receba três números e determine se o primeiro é menor que o
# segundo e maior que o terceiro utilizando operadores combinados.
# Descrição: O programa deve capturar três números e verificar a relação combinada entre eles usando
# operadores (<, >) em uma única expressão.

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 < numero2 and numero1 > numero3:
    print(f"{numero1} é menor que {numero2} e maior que {numero3}")
'''

'''
# Exercício 3:
# Enunciado: Crie um programa que receba a idade de uma pessoa e verifique se ela está apta a votar
# (idade maior ou igual a 16) ou a dirigir (idade maior ou igual a 18) usando operadores lógicos.
# Descrição: O programa deve capturar a idade do usuário, aplicar condições com operadores (and, or)
# e exibir as mensagens correspondentes às permissões.

idade = int(input("Digite sua idade: "))

if idade >= 16 and idade < 18:
    print("Você pode votar")
elif idade >= 18:
    print("Você pode votar e dirigir")
else:
    print("Você não pode votar e nem dirigir")
'''

'''
# Exercício 4:
# Enunciado: Escreva um programa que compare duas listas para verificar se elas ocupam o mesmo espaço
# na memória usando operadores de identidade (is) e verifique se um elemento específico está presente
# em ambas usando operadores de associação (in).
# Descrição: O programa deve criar duas listas, realizar a comparação de identidade com (is) e verificar
# a presença de um elemento em ambas as listas usando (in).


lista = ["Maçã", "Banana", "Goiaba", "Manga"]
lista2 = lista

el = "Goiaba"

print(lista is lista2)
print(el in lista and el in lista2)
'''

'''
# Exercício 5:
# Enunciado: Implemente um sistema de validação de login que verifica se o nome de usuário e a senha
# inseridos estão corretos, combinando operadores lógicos, de associação e de comparação.
# Descrição: O programa deve verificar se as credenciais inseridas pelo usuário coincidem com as
# credenciais armazenadas e exibir mensagens de sucesso ou erro.

login = input("Digite seu nome de usuario: ")
senha = int(input("Agora digite sua senha: "))

login_cadastrado = "abner123"
senha_cadastrada = 1234

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem vindo a página")
else:
    print("usuario e senha estão incorretos")
'''