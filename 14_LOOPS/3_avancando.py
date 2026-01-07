# Aula 1 - Loops aninhados
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in matriz:
    print(linha)
    for elemento in linha:
        print(f"Elemento: {elemento}")



lista1 = [1, 2, 3]
lista2 = [2, 5, 7]

for a in lista1:
    for b in lista2:
        if a == b:
            print(f"{a} é igual {b}")
        else:
            print(f"Comparando {a} e {b}")

marcas1 = ["samsung", "lg", "nokia"]
marcas2 = ["sony", "lg", "apple"]

for m in marcas1:
    for n in marcas2:
        if m == n:
            print(f"{m} é igual a {n}")
        else:
            print(f"Comparando {m} e {n}")

