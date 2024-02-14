#Diga se o número é primo ou não:
#Número primo é aquele número que é divisível apenas por 1 e por ele mesmo.

n = int(input('Digite um número: '))
total = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')

print(f'\n\033[mO número {n} foi divisível {total} vezes no total.')

if total == 2:
    print('Assim, ele é classificado como número primo.')
else:
    print('Assim, ele não é classificado como número primo.')