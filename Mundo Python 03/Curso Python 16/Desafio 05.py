lista = ('Lápis', 1.75,
         'Agenda', 13.50,
         'Borracha', 2.00,
         'Estojo', 18.00,
         'Canetas', 22.39,
         'Mochila', 130.32,
         'Livro', 34.90,
         'Leite', 4.50,
         'Frango', 20.90)

print('=-'*25)
print(' '*15, 'LISTA DE PREÇOS:')
print('=-'*25)

for posiçao in range(0, len(lista)):
    if posiçao % 2 == 0:
        print(f'{lista[posiçao]:.<30}', end='')
    else:
        print(f'R${lista[posiçao]}')