# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos. 
media = 0
mulher20 = 0
homemvelho = 0
nomevelho = ''

for c in range(1, 5):
    print(f'----- {c} PESSOA -----')
    nome = str(input('Digite o seu nome: ')).capitalize()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo (M/F): ')).upper()
    media += idade
    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
print('----- RESULTADO -----')
print(f'A média de idade do grupo é de {media / 4}.')
print(f'O homem mais velho do grupo é {nomevelho} e tem {homemvelho} anos.')
print(f'No total o grupo tem {mulher20} mulheres com menos de 20 anos.')