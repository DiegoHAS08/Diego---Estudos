valores = []

while True:
    n = int(input("Digite um valor: "))
    if n not in valores:
        valores.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")

    resp = input("Quer continuar? [S/N] ").strip().upper()
    if resp == 'N':
        break

valores.sort()
print(f"Você digitou os valores: {valores}")
