valores = []

for i in range(5):
    n = int(input("Digite um valor: "))
    if n not in valores:
        if len(valores) == 0 or n > valores[-1]:
            valores.append(n)
        else:
            pos = 0
            while pos < len(valores):
                if n < valores[pos]:
                    valores.insert(pos, n)
                    break
                pos += 1
        print("Valor adicionado com sucesso!")
    else:
        print("Valor já existe! Não será adicionado.")

print(f"Os valores digitados em ordem foram: {valores}")
