from time import sleep
#Descobrindo o maior valor com funções.

def maior(* num):
    cont = maior = 0
    print('=-' *30)
    print('\nAnalisando os valores passados... ')
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nForam informados {cont} valores no total.')
    print(f'O maior valor informado foi {maior}.')


# Programa Principal
maior(2, 9, 4, 5, 7)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()