mais18 = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo: [M/F] ')).upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('Você deseja prosseguir? [S/N] ')).upper()
    if continuar == 'N':
        print(f'No total são {mais18} pessoas maior de 18 anos.')
        print(f'No total são {homens} homens.')
        print(f'No total são {mulheres} mulheres com menos de 20 anos.')
        break