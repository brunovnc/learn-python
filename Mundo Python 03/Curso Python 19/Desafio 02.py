from random import randint
from operator import itemgetter

jogadas = {'jogador1':randint(1, 6), 
           'jogador2':randint(1, 6), 
           'jogador3':randint(1, 6), 
           'jogador4':randint(1, 6)}
ranking = []

print('Dados sorteados:')
for j, v in jogadas.items(): #Para cada jogador, valor em jogadas, print o Resultado.
    print(f'{j} = Dado {v}')

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) #O itemgetter serve para pegar uma key ou item específico de um dicionário.

print('Ranking:')
for i, v in enumerate(ranking): #Para cada indice, valor em jogadas, enumerar o ranking. (Enumarate pois é uma lista, e não um dicionário)
    print(f'{i+1}° lugar = {v[0]} com Dado {v[1]}.')
