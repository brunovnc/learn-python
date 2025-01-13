# Crie um programa que leia dois valores e mostre um menu na tela:
# 1: Somar
# 2: Multiplicar
# 3: Maior
# 4: Novos números
# 5: Sair do programa
import time
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

maior = 0
menu = 0

while menu != 5:
    print('========MENU========')
    menu = int(input('[1] Somar \n[2] Multiplicação \n[3] Maior número \n[4] Novos números \n[5] Sair \nDigite uma opção:'))
    if menu == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1 + n2}.')
        break
    if menu == 2:
        print(f'A multiplicação de {n1} x {n2} é igual a {n1 * n2}.')
        break
    if menu == 3 and n1 > n2:
        print(f'O maior número é {n1}.')
        break
    elif menu == 3 and n2 > n1:
        print(f'O maior número é {n2}.')
        break
    if menu == 4:
        print('Reiniciando...')
        time.sleep(1)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    print('Encerrando...')