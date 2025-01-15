# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será encerrado se o número digitado for negativo.

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('Encerrando...')
        break
    for c in range(0,11):
        print(f'{n} x {c} = {n * c}')