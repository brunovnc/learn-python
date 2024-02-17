n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
n4 = int(input('Digite o último valor: '))

numeros = (n1, n2, n3, n4)

print(f'Os números inseridos foram: {numeros}.')
print('=-'*30)

print(f'No total o número 9 foi inseridos {numeros.count(9)} vezes.')
print('=-'*30)

for n in numeros:
    if n == 3:
        print(f'O primeiro número 3 foi inserido na posição {numeros.index(3)}.')
print('=-'*30)

print('Os números pares inseridos são: ', end='')
for n in numeros:
    if n % 2 == 0:
     print(f'{n}', end=' ')