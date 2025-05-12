num = s = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    s += num
print(f"A soma dos valores foi {s}.")