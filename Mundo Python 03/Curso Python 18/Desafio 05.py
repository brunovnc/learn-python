import random
import time

lista = []
jogos = []
print('-'*30)
print('      JOGO DA MEGA SENA:')
print('-'*30)
quantidade = int(input('Digite quantos jogos você quer que eu sorteei: '))
total = 1

while total <= quantidade: #Se o contador total atingir a quantidade de jogadas sorteadas que foram inseridas, break.
    contador = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6: #Ao atingir 6 números no contados, break.
            break
    lista.sort()
    jogos.append(lista[:]) #Copia a lista temporária pra lista principal "jogos" e depois clear.
    lista.clear()
    total += 1 #Quando o total atingir a quantidade de jogadas, encerra.
print(f'-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print(f'-=-=-=-=-= < BOA SORTE! > =-=-=-=-=')