# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
import random

print('Estou pensando em um número de 0 a 5 e você vai tentar advinhar! ')
n = int(input('Qual desses números estou pensando? '))

sorteio = random.randint(0, 5)

if n == sorteio:
    print('Você ganhou o jogo! ')
else: 
    print(f'Você perdeu o jogo! O número que pensei foi {sorteio}.')