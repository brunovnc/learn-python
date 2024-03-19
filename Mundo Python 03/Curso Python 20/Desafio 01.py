def area(l, c):
    print('-' *20)
    print('Controle de Terrenos:')
    print('-' *20)
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    t = l * c
    print(f'A área do terreno ({l}x{c}) é de {t}m².')
def linha():
    print('-' *30)

# Programa Principal
area(0, 0)
linha()