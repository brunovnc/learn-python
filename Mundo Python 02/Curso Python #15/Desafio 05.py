contador = 0
valortotal = 0
maisdemil = 0
barato = 0
nomebarato = ''

while True:
    nome = str(input('Digite o nome do produto: ')).upper()
    preço = float(input('Digite o preço do produto: '))
    continuar = str(input('Você deseja continuar com o cadastro? [S/N]')).upper()
    valortotal += preço
    contador += 1
    if preço > 1000:
        maisdemil += 1
    if contador == 1:
        barato = preço
        nomebarato = nome
    else:
        if preço < barato:
            barato = preço
            nomebarato = nome
    if continuar == 'N':
        print(f'O valor total gasto foi de R${valortotal:.2f}.')
        print(f'No total foram comprados {maisdemil} produtos que custam mais de R$1000,0.')
        print(f'O produto mais barato comprado foi {nomebarato} que custa R${barato}.')
        break