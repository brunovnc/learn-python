matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um valor: '))
print('=-'*30)

print(matriz[0])
print(matriz[1])
print(matriz[2])

print('=-'*30) #OU

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()