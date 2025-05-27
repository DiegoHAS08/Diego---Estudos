# Exercício 81 - Extraindo dados de uma Lista

valores = list()
for i in range(5):
    num = int(input(f"Digite um valor para a posição {i}: "))
    valores.append(num)

print(f"Você digitou os valores: {valores}")
print(f"O maior valor foi {max(valores)} nas posições:", end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(i, end=' ')
print(f"\nO menor valor foi {min(valores)} nas posições:", end=' ')
for i, v in enumerate(valores):
    if v == min(valores):
        print(i, end=' ')
