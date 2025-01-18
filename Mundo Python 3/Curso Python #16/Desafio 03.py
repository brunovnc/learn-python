# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique e menor e o maior valor que estão na tupla.
import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
         random.randint(1, 10), random.randint(1, 10))
maior = menor = 0

print(f'Números: ', end='')
for c in (tupla):
    if c == tupla[0]:
        maior = c
        menor = c
    if c > maior:
        maior = c
    if c < menor:
        menor = c
    print(f'{c}', end=' ')
print(f'\nO maior número é {maior}. \nO menor número é {menor}.')