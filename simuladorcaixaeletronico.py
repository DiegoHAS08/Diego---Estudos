print("==== Caixa Eletrônico ====")
valor = int(input("Que valor você quer sacar? R$ "))
cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula
    if quantidade > 0:
        print(f"Total de {quantidade} cédula(s) de R$ {cedula}")
