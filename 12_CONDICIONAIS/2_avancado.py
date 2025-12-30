# Aula 1 - Condicionais aninhadas
idade = 22

if idade >= 18:
    print("Você é maior de idade!")
    if idade > 21:
        print("Você pode beber nos EUA")
    else: 
        print("Você não pode beber nos EUA")
else:
    print("Você é menor de idade!")

nota = 10

if nota >= 7:
    print("Você foi aprovado")
    if nota == 10:
        print("Parabéns você tirou a nota maxima.")
else:
    print("Você ficou de recuperação")

lista = [1, 2, 3]

if len(lista) > 0:
    print("A lista não está vazia")
    if 2 in lista:
        print("O número 2 está na lista") 
else:
    print("Sua lista está vazia")

x = 30
y = 20
z = 20

# Aula 2 - Combinacao de condições e op. lógicos
idade = 22
renda = 800

if idade > 18 and renda < 1800: 
    print("Você está cadastrado no programa")

usuario = 'teste1234'
senha = "minhasenha"

if usuario == "teste1234" and senha == "minhasenha1":
    print("Loggin com sucesso")
else:
    print("Credencias erradas")

x = 11
y = 20 
z = 20

if x < y or y < z and x == 10: # resultado é "Condição verdadeira" por que umas das comparações do or deu True
    print("Condição verdadeira")
else:
    print("deu errado")

if (x < y or y < z) and x == 10: # já aqui o resultado é False
    print("Condição verdadeira")
else:
    print("deu errado")

# Aula 3 - operadores ternarios
idade = 20

resultado = "Maior de idade" if idade >= 18 else "Menor de idade" 

print(resultado)

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

numero = 8 

paridade = "O número é par" if numero % 2 == 0 else "O número não é par"

print(paridade)

frutas = ["BANANA", "MAÇÂ", "LARANAJA"]

quantidade_suficiente = "A quantidade de frutas é suficiente" if len(frutas) >= 5 else "Compre mais frutas"

print(quantidade_suficiente)
# VALOR SE IF FOR TRUE if CONDIÇÂO A SER AVALIADA else VALOR SE IF FOR FALSO
# Use operadores ternarios em operações simples

# Aula 4 - Evitando ifs aninhados, elifs ecelse desnecessarios 

def verificador_idade(idade):
    if idade < 18:
        return "Menor de idade"
    
    return "Maior de idade"
print(verificador_idade(18))

def verifica_cor(cor):
    if cor != "verde":
        return "Cor invalida"
    
    return "Cor correta"

print(verifica_cor("azul")) 

opcao = {
    "vermelho": "Pare",
    "amarelo": "Atenção",
    "verde": "Siga"
}

cor = input("Digite uma cor (verde, vermelho ou amarelo) ")

print(opcao.get(cor, "Cor invalida"))

idade = 18
renda = 3000

if idade >= 18:
    if renda > 2000:
        print("Elegivel ao beneficio")

if idade >= 18 and renda > 2000:
    print("Elegivel ao beneficio")