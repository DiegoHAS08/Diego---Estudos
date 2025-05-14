total_maior_idade = total_homens = mulheres_menos_20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    if idade > 18:
        total_maior_idade += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print(f"\nTotal de pessoas com mais de 18 anos: {total_maior_idade}")
print(f"Total de homens cadastrados: {total_homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}")
