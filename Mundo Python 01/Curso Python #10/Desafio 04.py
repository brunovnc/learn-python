km = float(input('A viagem será de quantos KM?'))
if km <=200.0:
    valortotal = (km * 0.50)
    print(f'Sua viagem custará no total R${valortotal}.')
else:
    valortotall = (km * 0.45)
    print(f'Sua viagem custará no total R${valortotall}.')