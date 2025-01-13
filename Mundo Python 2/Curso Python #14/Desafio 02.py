# Melhore o jogo de advinhação onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai tentar advinhar até acertar.
# Mostre no final quantos palpites foram necessários para vencer.
import random
n = int(input('Vou pensar em um número de 0 a 10. Tente advinhar: '))

sorteio = random.randint(0, 10)
contador = 0

while n != sorteio:
    print('Você errou HAHA! Tente novamente.')
    n = int(input('Digite um número de 0 a 10: '))
    sorteio = random.randint(0, 10)
    contador += 1
print(f'Parabéns! Você ganhou o jogo. Total de tentativas: {contador + 1}.')