#Faça o computador jogar jokenpô com você:
import random

jokenpo = (input('Pedra, papel ou tesoura? ')).lower()

computador = random.choice(['pedra', 'papel', 'tesoura'])
print(f'Máquina: {computador}.')

if jokenpo == 'pedra' and computador == 'pedra':
    print('Empate! Joguem novamente!')
elif jokenpo == 'tesoura' and computador == 'tesoura':
    print('Empate! Joguem novamente!')
elif jokenpo == 'papel' and computador == 'papel':
    print('Empate! Joguem novamente!')

elif jokenpo == 'pedra' and computador == 'papel':
    print('A máquina foi a vencedora dessa rodada!')
elif jokenpo == 'papel' and computador == 'pedra':
    print('Você foi o vencedor dessa rodada!')

elif jokenpo == 'pedra' and computador == 'tesoura':
    print('Você foi o vencedor dessa rodada!')
elif jokenpo == 'tesoura' and computador == 'pedra':
    print('A máquina foi a vencedora dessa rodada!')

elif jokenpo == 'papel' and computador == 'tesoura':
    print('A máquina foi a vencedora dessa rodada!')
elif jokenpo == 'tesoura' and computador == 'papel':
    print('Você foi o vencedor dessa rodada!')

#ou
    
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print(f'A máquina escolheu: {(itens[computador])}')