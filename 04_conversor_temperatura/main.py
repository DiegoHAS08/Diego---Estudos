def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

print("Conversor de Temperatura")
opcao = input("Converter para (F)ahrenheit ou (C)elsius? ").upper()
valor = float(input("Digite o valor: "))

if opcao == "F":
    print(f"{valor}°C = {celsius_para_fahrenheit(valor):.2f}°F")
elif opcao == "C":
    print(f"{valor}°F = {fahrenheit_para_celsius(valor):.2f}°C")
else:
    print("Opção inválida.")