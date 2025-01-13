# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5x4x3x2x1 = 120
import math
n = int(input('Digite um número: '))
contador = n - 1

print(f'{n}', end='')
while contador != 0:
    print(f'x{contador}', end='')
    contador -= 1
print(f' = {math.factorial(n)}')

# OU

n2 = int(input('Digite um número: '))
multiplicador = n2 - 1

print(n2, end='')
for c in range(1, n2):
    print(f'x{multiplicador}', end='')
    multiplicador -= 1
print(f' = {math.factorial(n2)}')