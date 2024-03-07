time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    total = int(input('Total de Partidas: '))
    partidas.clear()
    print('TOTAL DE GOLS POR PARTIDA:')
    for c in range(0, total):
        partidas.append(int(input(f'{c+1}° Partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas) #sum serve para somar os valores de uma LISTA.
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

print('=-'*20)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 BREAK] '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro!')
    else:
        print(f'- Levantamento do jogador {time[busca]["nome"]}')