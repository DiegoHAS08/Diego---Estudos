def calculadora():
    while True:
        operacao = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
        if operacao == 'sair':
            print("Encerrando calculadora.")
            break
        
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue

        if operacao == '+':
            print("Resultado:", a + b)
        elif operacao == '-':
            print("Resultado:", a - b)
        elif operacao == '*':
            print("Resultado:", a * b)
        elif operacao == '/':
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Erro: Divisão por zero")
        else:
            print("Operação inválida.")

calculadora()
