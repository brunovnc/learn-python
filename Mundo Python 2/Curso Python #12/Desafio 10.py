# Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time
jokenpo = str(input('Pedra, papel ou tesoura? ')).upper()
maquina = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

print('Jo...')
time.sleep(1)
print('Ken...')
time.sleep(1)
print('Pô...')
print(f'{maquina}!')

if jokenpo == 'PAPEL' and maquina == 'TESOURA':
    print('Você perdeu o jogo! HAHAHA')
elif jokenpo == 'PAPEL' and maquina == 'PEDRA':
    print('Parabéns! Você venceu o jogo!')
elif jokenpo == 'TESOURA' and maquina == 'PEDRA':
    print('Você perdeu o jogo! HAHAHA')
elif jokenpo == 'TESOURA' and maquina == 'PAPEL':
    print('Parabéns! Você venceu o jogo!')
elif jokenpo == 'PEDRA' and maquina == 'TESOURA':
    print('Parabéns! Você venceu o jogo!')
elif jokenpo == 'PEDRA' and maquina == 'PAPEL':
    print('Você perdeu o jogo! HAHAHA')
else:
    print('Foi um empate! Tente novamente.')