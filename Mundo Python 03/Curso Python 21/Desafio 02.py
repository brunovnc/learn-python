def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não o cálculo.
    :return: O valor do Fatorial de um número n.
    """
    f = 1 #Se começar por 0 a multiplicação vai dar 0.
    print(f'Calculando {n}...')
    for c in range (n, 0, -1):
        if show == True: #se show for True, mostrar.
            print(f'{c}', end='')
            if c > 1: #Se "c" for maior que 1, aparece X (mulplicando), se for menor que 1 aparece =.
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f += c
    return f


# Programa Principal
print(fatorial(5, show=True))

#help(fatorial)