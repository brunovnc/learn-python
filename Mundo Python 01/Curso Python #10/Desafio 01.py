import random
print('Pensando em um número de 0 a 5...')
numescolhido = random.choice([0, 1, 2, 3, 4, 5])

num = int(input('Qual número de 0 a 5 estou pensando agora?'))

print(f'O número que estou pensando é o {numescolhido}.')
if numescolhido == num:
    print('Você acertou o número que estava pensando!')
else:
    print('Você errou o número que estava pensando! :(')
