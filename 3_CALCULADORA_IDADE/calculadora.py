# baseado no ano de nascimento do usuario
# calcular a idade dele
# 2025 ou 2026

from datetime import datetime

# datetime -> um biblioteca do python com varias funcionalidades para lidar com datas

ano_atual = datetime.now().year

ano_nascimento = int(input("Em que ano você nasceu?"))

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos")