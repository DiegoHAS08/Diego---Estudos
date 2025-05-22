numeros = []

for i in range(5):
    n = int(input(f"Digite um número para a posição {i}: "))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

print(f"\nVocê digitou os valores: {numeros}")
print(f"O maior valor digitado foi {maior} nas posições:", end=" ")
for i, v in enumerate(numeros):
    if v == maior:
        print(i, end=" ")

print(f"\nO menor valor digitado foi {menor} nas posições:", end=" ")
for i, v in enumerate(numeros):
    if v == menor:
        print(i, end=" ")
