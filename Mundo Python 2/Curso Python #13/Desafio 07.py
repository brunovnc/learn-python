# Faça um programa que leia um número inteiro e diga se ele é um número primo ou não.
n = int(input('Digite um número inteiro: '))

if n == 2:
    print(f'{n} é um número primo.')
elif n % 3 == 0:
    print(f'{n} não é um número primo.')
elif n > 2 and n % 2 == 0:
    print(f'{n} não é um número primo.')
elif n > 5 and n % 5 == 0:
    print(f'{n} não é um número primo.')
elif n > 7 and n % 7 == 0:
    print(f'{n} não é um número primo.')
else:
    print(f'{n} é um número primo.')

# OU

num = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

if total == 2:
    print(f'\nO número {num} foi divisível {total} vezes. Logo, é um número primo.')
else:
    print(f'\nO número {num} foi divisível {total} vezes. Logo, não é um número primo.')