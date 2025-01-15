# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra;
# Quantos produtos custam mais de R$1000;
# Qual é o nome do produto mais barato.
total = 0
maiormil = 0
menor = 0
produtobarato = ''

while True:
    nome = str(input('Digite o nome do produto: ')).capitalize()
    preco = float(input('Digite o preco do produto: R$'))
    if preco > 1000:
        maiormil += 1
    if total == 0:
        menor = preco
    if preco < menor:
        menor = preco
        produtobarato = nome
    total += preco
    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if continuar == 'N':
        print(f'No total foram gastos na compra R${total}. \nNo total {maiormil} produtos custam acima R$1000,0. \nO produto mais barato é o {produtobarato}.')
        break
