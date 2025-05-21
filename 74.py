from random import randint
numeros = tuple(randint(1, 100) for _ in range(5))
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')