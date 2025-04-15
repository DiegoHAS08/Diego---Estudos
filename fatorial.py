# fatorial.py

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

def main():
    print("=== Calculadora de Fatorial ===")
    try:
        numero = int(input("Digite um número para calcular o fatorial: "))
        if numero < 0:
            print("Fatorial não existe para números negativos!")
        else:
            print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
    except ValueError:
        print("Digite um número válido.")

if __name__ == "__main__":
    main()
