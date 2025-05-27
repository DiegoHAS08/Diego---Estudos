# Exercício 85 - Listas com pares e ímpares

num = [[], []]
for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f"Pares: {num[0]}")
print(f"Ímpares: {num[1]}")
