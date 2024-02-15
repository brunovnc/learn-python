import random
print('=-'*25)
print('Vou pensar em um número de 0 a 5. Tente advinhar!')
print('=-'*25)

computador = random.randint(0, 5)
palpites = 0

resposta = int(input('Digite um número: '))

while resposta != computador:
    print(f'Você errou! O número que a máquina pensou foi: {computador}')
    computador = random.randint(0, 5)
    resposta = int(input('Tente novamente! Digite um número: '))
    palpites += + 1
print(f'Você acertou o número! No total foram {palpites} palpites.')