brasileirao = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthias', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print(f'Os 5 primeiros colocados são {brasileirao[0:5]}.')
print('-='*20)
print(f'Os últimos 4 colocados são {brasileirao[-4:]}.')
print('-='*20)
print(sorted(brasileirao)) #Lista em ordem alfabética.
print('-='*20)

for posiçao, time in enumerate(brasileirao): #Qual a posição o Fluminense está na tabela.
    if time == 'Fluminense':
        posiçao -= 1
        print(f'O time {time} está na {posiçao}° posição do Brasileirão Série A.')
print('Desafio encerrado!')
#ou 
print(f'O Internacional está na {brasileirao.index("Internacional")}° posição do Brasileirão Série A.')
