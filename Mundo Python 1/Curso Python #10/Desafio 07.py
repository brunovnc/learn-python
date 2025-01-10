# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = int(input('Digite o valor de um lado do triângulo em cm: '))
l2 = int(input('Digite o valor outro lado do triângulo em cm: '))
l3 = int(input('Digite o valor mais outro lado do triângulo em cm: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print('É possível formar um triângulo com esses valores.')
else:
    print('Não é possível formar um triângulo com esses valores.')