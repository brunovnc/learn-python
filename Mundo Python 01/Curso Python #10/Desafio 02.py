velocidade = int(input('Qual a velocidade em km do carro?'))
multa = (7 * velocidade)

if velocidade >=80:
    print(f'Alerta de alta velocidade! Você foi multado em R${multa} por andar a {velocidade}km/h em uma pista de 80km/h.')
else:
    print('Tudo OK! A sua velocidade está dentro dos limites estabelecidos.')