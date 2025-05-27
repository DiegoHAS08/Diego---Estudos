# Exercício 87 - Mais sobre Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna_3 = maior_linha_2 = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))

print('-=' * 20)
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

print('-=' * 20)
print(f"A soma dos valores pares é {soma_pares}")
for l in range(3):
    soma_coluna_3 += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {soma_coluna_3}")

maior_linha_2 = max(matriz[1])
print(f"O maior valor da segunda linha é {maior_linha_2}")
