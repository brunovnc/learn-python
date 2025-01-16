# Crie uma tupla preenchida com os 20 primeiros coolocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados;
# Os últimos 4 colocados da tabela;
# Uma lista com os times em ordem alfabética;
# Em que posição na tabela está o time Chapecoense.
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthias', 'Bahia', 'Cruzeiro', 'Vasco',
         'Chapecoense', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletco-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'Lista de times do Brasileirão: {times}.')
print('-='*15)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos times são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')