# Crie um programa que leia vários números inteiros no teclado. O programa só para quando digitar 999. No final, mostre quantos números foram digitados e a soma entre eles.
n = int(input('Digite um número (Digite 999 para encerrar): '))

cont = 0
soma = 0

while True:
    cont += 1
    soma += n
    n = int(input('Digite um número (Digite 999 para encerrar): '))
    if n == 999:
        print(f'Foram apresentados no total {cont} números.')
        print(f'A soma entre todos os número é {soma}.')
        break