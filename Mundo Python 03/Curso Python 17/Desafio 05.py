lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
        print('Esse número é par.')
    if n % 2 == 1:
        listaimpar.append(n)
        print('Esse número é impar.')
    continuar = str(input('Você deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break    
print(f'Lista completa: {lista}.')
print(f'Lista com números par: {listapar}.')
print(f'Lista com números impar: {listaimpar}.')