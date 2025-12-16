# Gerar um numero aleatorio
# Verificar se o usuario acertou
# Contabilizando as tentativas

import random

def jogo_adivinhacao():
    print("BEM-Vindo ao Jogo de Advinhação")
    print("Tente advinhar um número aleatório de 1 a 100")
    print("É permitido no máximo 8 tentativas")

    # Gerar o numero aleatorio
    numero_secreto = random.randint(1, 100)

    # Inicializar variaveis que vão ajudar o sistema a contabilizar as jogadas
    tentativas = 0
    acertou = False

    while not acertou:
        while tentativas < 8:
            tentativas += 1
            

            palpite = int(input("Digite um número: "))

            if palpite == numero_secreto:
                print(f"Parabéns você acertou o número secreto {numero_secreto} na sua {tentativas}° tentativa.")
                acertou = True
                break

            elif palpite > numero_secreto:
                print("O número secreto é menor. Tente novamente")
            
            else:
                print("O número secreto é maior. Tente novamente")

        else:
            print("Game OVER")
            acertou = True

if __name__ == "__main__":
    jogo_adivinhacao()