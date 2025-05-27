# Exercício 82 - Dividindo valores em várias listas

numeros = [[], []]
for i in range(7):
    n = int(input(f"Digite o {i+1}º valor: "))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()
print(f"Pares: {numeros[0]}")
print(f"Ímpares: {numeros[1]}")
