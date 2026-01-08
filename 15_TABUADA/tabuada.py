"""
    Gerar a tabuada de um número fornecido pelo usuário, exibindo os resultados de 1 a 10.
"""

def tabuada():
    print("Bem-vindo a tabuada!")

    numero = int(input("Por favor, insira um número inteiro válido: "))

    print(f"Exibindo a multiplicação do número {numero}")

    for n in range(1, 11):
        print(f"{numero} X {n} = {numero * n}")
        
if __name__ == "__main__":
    tabuada() 