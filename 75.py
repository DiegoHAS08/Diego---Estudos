valores = tuple(int(input(f'Digite o {i+1}º valor: ')) for i in range(4))
print(f'Você digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Números pares digitados: {[n for n in valores if n % 2 == 0]}')