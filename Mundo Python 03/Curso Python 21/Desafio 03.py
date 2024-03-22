def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g == '' or not g.isnumeric():
        g = '<não informado>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = input('N° Gols: ')
ficha(n, g)