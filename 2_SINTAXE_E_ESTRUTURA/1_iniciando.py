# Aula 1
print("Meu texto")

# 1. def é usado para criar uma função
# 2. a instrução if__name__ == "__main__", faz com que o programa se em um determinado local 

def saudacao():
    print("Minha saudação")

if __name__ == "__main__":
    saudacao() 

# Aula 2 - Indentação
if 10 > 15: 
    print("10 realmente é maior 5")
    print("Operação finalizada")
    print("Terminando o if")

#  Aula 3 - Blocos em Python
if 70 > 18:
    print("Você é maior de idade")
    if 70 > 65: 
        print("Você é considerado idoso")

# Aula 4 - Comentários 

# Aulas 5 - Função print
print("Exibir uma mensagem")

print("Exibir", "Mensagem")

print("Laranja", "Maçã", "Banana", sep=" - ")

print("Carregando",  end="...")