valores = []

for contador in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {contador}: ')))

print('=-' *30)
print(f'Você digitou os valores: {valores}.')
print('=-' *30)

print(f'O maior valor é {max(valores)}', end=' ')
print(f'e está na posição ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}', end=' ')

print(f'\nO menor valor é {min(valores)}', end=' ')
print(f'e está na posição ', end='')
for p2, v2 in enumerate(valores):
    if v2 == min(valores):
        print(f'{p2}', end=' ')
print('\nDesafio encerrado!')