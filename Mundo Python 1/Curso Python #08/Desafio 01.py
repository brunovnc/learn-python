# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Exemplo: 6.127 > 6

n = float(input("Digite um número real: "))
inteira = str(n)

print(f'A porção inteira do número {n} é igual a {inteira[0]}.')

# OU

import math

num = float(input("Digite um número real: "))

print(f'A porção inteira do número {num} é igual a {math.trunc(num)}.')

# OU

num2 = float(input("Digite um número real: "))

print(f'A porção inteira do número {num2} é igual a {int(num2)}.')