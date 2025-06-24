def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

if __name__ == "__main__":
    print("Calculadora Básica")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")

    if op == "+":
        print("Resultado:", soma(a, b))
    elif op == "-":
        print("Resultado:", subtrai(a, b))
    elif op == "*":
        print("Resultado:", multiplica(a, b))
    elif op == "/":
        print("Resultado:", divide(a, b))
    else:
        print("Operação inválida")