# conversor_temperatura.py

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("=== Conversor de Temperatura ===")
    escolha = input("Deseja converter de Celsius para Fahrenheit ou vice-versa? (C/F): ").lower()
    
    if escolha == 'c':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F")
    elif escolha == 'f':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit)}°C")
    else:
        print("Escolha inválida. Digite 'C' ou 'F'.")

if __name__ == "__main__":
    main()
