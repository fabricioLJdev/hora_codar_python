# Aula 1 - operadores

# OPERACOES COM OPERADORES LOGICOS RESULTAM EM BOOLEANOS (TRUE OU FALSE)

a = 5
b = 10

print(a == b)
print(a != b)

# > -> maior que 
# < -> menor que
print(a > b)
print(b > a)
print(a < b)

c = 10 
d = 11

# >= ou <= TB valida a igualdade entre eles 
print(b >= c)
print(b > c)
print(a <= d)

# não vai levar a gente para lugar nenhum
print("maçã" > "banana")

# isso aqui abaixo é ok 
print(len("maçã") > len("banana"))

# Aula 2 - continuando operadores
x = 10
y = 15

# *** Lembra que sempre o resultado de uma comparação com operadores é booleano ***
print(x != y)

z = 20

# composição de comparação
print(x < y < z) # todas comparações tem que ser verdadeiras para retornar true

# Comparar tipos de dados diferentes
valor = "5"
x = 5

print(valor == x)

print(int(valor) == 5)

# gera um erro: print(valor > x). Dados diferentes 

# Aula 3 - operadores lógicos 
idade = 25

print(idade > 18 and idade < 30) # é como se and decidisse qual é o retorno do booleano

idade = 22

print(idade < 18 or idade > 65)

# and => precisa dos dois lados como true
# or => precisa de um dos lados como true


a = 10 
b = 5 
c = 6
d = 7 

# not faz que o valor do booleano seja inverso 

print(a > b or c == d)

print(not a > b or c == d)