# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos;
# Quantos homens foram cadastrados;
# Quantas mulheres tem menos de 20 anos.
maior18 = 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Digite o seu sexo [M/F]: ')).upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if idade > 18:
        maior18 += 1
    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        print(f'FORAM CADASTRADAS: \n{maior18} Pessoas maiores de 18 anos. \n{homens} Homens no total. \n{mulheres20} Mulheres menores de 20 anos.')
        break