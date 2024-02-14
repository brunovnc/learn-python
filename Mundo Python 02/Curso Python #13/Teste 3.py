n = int(input('Digite um número: '))
total = 0

for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')

print(f'\n\033[mO número {n} foi divisível {total} vezes no total.')

if total == 2:
    print('Assim, não é classificado como número primo.')
else:
    print('Assim, é classificado como número primo.')