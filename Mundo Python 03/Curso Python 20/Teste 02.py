def contador(* num):
    for v in num:
        print(f'{v} ', end='')
    print('FIM!')
def teste(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')
def linha():
    print('-' *30)


# Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
linha()
teste(2, 1, 7)
teste(8, 0)
teste(4, 4, 7, 6, 2)
#Os elementos são jogados em num, e são criadas Tuplas.