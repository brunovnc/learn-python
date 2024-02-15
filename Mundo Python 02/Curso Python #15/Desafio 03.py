import random
import time

print('=-'*15)
print('       PAR OU IMPAR:')
print('=-'*15)

contador = 0

while True:
    n = str(input('Digite Par ou Impar? ')).upper()
    time.sleep(1)
    n2 = int(input('um dolasi e já! [0-10] '))
    maquina = random.randint(0, 10)
    soma = n2 + maquina
    print(f'Você jogou {n2} e a máquina {maquina}.')
    if soma % 2 == 0 and n == 'PAR' or soma % 2 == 1 and n == 'IMPAR':
        print('O jogador venceu a rodada.')
        contador += 1
    else:
        print('A máquina venceu a rodada. Você perdeu!')
        break
print(f'Você teve um total de {contador} vitórias.')