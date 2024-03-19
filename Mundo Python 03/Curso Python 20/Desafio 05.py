import random
numeros = []

def sorteio():
    print(f'Os números sorteados foram: ')
    for c in range(0, 5):
        n = random.randint(1, 10)
        numeros.append(n)
        print(f'{n}', end=' ')
def somapar():
    totalpar = 0
    for v in numeros:
        if v % 2 == 0:
            totalpar += v
    print(f'\nA soma dos números pares é {totalpar}.')


# Programa Principal
sorteio()
somapar()