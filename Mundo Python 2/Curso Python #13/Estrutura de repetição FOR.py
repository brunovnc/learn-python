for c in range(0, 3):
    print('Yeah Brother!')
    print('Yeah Sr.')
print('Goodbye!')

print('---------------------------')

contador = 0
for c in range(0, 3):
    print('Olá, Mundo!')
    contador += 1
    if contador == 3:
        print('O contador estorou!')
print('Encerrando...')

print('---------------------------')

for c in range(6, 0, -1):
    print(c)
print('FIM!')

print('---------------------------')

for c in range(0, 7, 2):
    print(c)
print('FIM!')

print('---------------------------')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM!')

print('---------------------------')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}.')