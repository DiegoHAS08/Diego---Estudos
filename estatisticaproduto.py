total_gasto = produto_mais_1000 = menor_preco = 0
nome_mais_barato = ''

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))

    total_gasto += preco
    if preco > 1000:
        produto_mais_1000 += 1
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = nome

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print(f"\nTotal gasto na compra: R$ {total_gasto:.2f}")
print(f"Produtos que custam mais de R$1000: {produto_mais_1000}")
print(f"O produto mais barato foi '{nome_mais_barato}' que custa R$ {menor_preco:.2f}")
