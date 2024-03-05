dados = {}
gols = []

dados['Jogador'] = str(input('Nome do Jogador: '))
Partidas = int(input('Total de Partidas: '))

print('TOTAL DE GOLS POR PARTIDA:')
for g in range(0, Partidas):
    gols.append(int(input(f'{g+1}° Partida: ')))
dados['Gols'] = gols
dados['Total'] = sum(gols) #sum serve para somar os valores de uma LISTA.

print('=-'*20)
print('ESTATÍSTICAS:')
print(f'O jogador {dados['Jogador']} participou de {Partidas} partidas.')
for i, g in enumerate(gols):
    print(f'  => Na partida {i+1}, fez {g} gols.')
print(f'Foi um total de {dados['Total']} gols.')