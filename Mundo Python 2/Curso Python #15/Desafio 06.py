# Crie um programa de Caixa Eletrônico. Pergunte qual será o valor a ser sacado (nº inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Digite o valor do saque (nº inteiro): R$'))

c50 = 0
c20 = 0
c10 = 0
c1 = 0
totalvalor = valor

while True:
    if valor >= 50:
        c50 += 1
        valor -= 50
    elif valor >= 20 and valor < 50:
        c20 += 1
        valor -= 20
    elif valor >= 10 and valor < 20:
        c10 += 1
        valor -= 10
    elif valor >= 1 and valor < 10:
        c1 += 1
        valor -= 1
    if valor == 0:
        print(f'O valor total sacado foi de R${totalvalor}. Serão entregues: \n{c50} Cédulas de R$50 \n{c20} Cédulas de R$20 \n{c10} Cédulas de R$10 \n{c1} Cédulas de R$1')
        break