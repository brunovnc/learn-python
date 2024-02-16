import random
numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), 
     random.randint(1, 10), random.randint(1, 10))

print(f'Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

print(f'\nO maior valor é {max(numeros)} e o menor valor é {min(numeros)}.')