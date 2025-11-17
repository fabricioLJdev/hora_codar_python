# Receber um texto
# E determinar quantas: palavras, caracteres e linhas o texto tem!

def analisar_texto(texto):
    #contar linhas
    linhas = texto.splitlines()
    numero_linha = len(linhas)

    # contar palavras
    palavras = texto.split()
    numero_de_palavras = len(palavras)

    # contar caracteres
    numero_de_caracteres = len(texto)

    return numero_linha, numero_de_palavras, numero_de_caracteres

def main():
    print("Bem-vindo ao Analizador de Textos!")
    print("Digite o seu texto abaixo, e para finalizar pressione Enter duas vezes")

    # Entrada de Texto
    texto = ""
    while True:
        linha = input()
        # Condição de encerramento
        if linha == "":
            break
        texto += linha + "\n"
    
    linhas, palavras, caracteres = analisar_texto(texto)

    print("Resultado da análise:")
    print(f"Numero de linhas: {linhas}")
    print(f"Numero de palavras: {palavras}")
    print(f"Numero de caracteres: {caracteres}")


if __name__ == "__main__":
    main()