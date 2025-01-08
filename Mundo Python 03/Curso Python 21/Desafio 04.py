def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número válido\033[m')


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')