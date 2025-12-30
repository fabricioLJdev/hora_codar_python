"""
    Calcular o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos pelo usuário,
    e classifica o resultado em categorias pré-definidas.
"""

def calculadora_imc():
    print("Bem-vindo a calculadora de IMC!")

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    imc = peso / (altura ** 2)

    print(f"Seu é IMC é {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")

    elif imc < 24.9:
        print("Classificação: Peso normal")

    elif imc < 29.9:
        print("Classificação: Sobrepeso.")

    elif imc < 34.9:
        print("Classificação: Obesidade Grau 1")

    elif imc < 39.9:
        print("Classificação: Obesidade Grau 2")

    else:
        print("Obesidade Mórbida")
        
if __name__ == "__main__":
    calculadora_imc()