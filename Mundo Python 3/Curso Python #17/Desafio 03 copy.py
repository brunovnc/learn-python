# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta (sem usar o sort()). No fim, mostre a lista ordenada.
lista = []
comparador = 0

for c in range(0, 5):
    n = (int(input('Digite um valor: ')))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    elif c == 1 and n < lista[0]:
        lista.insert(0, n)
    elif c == 2 and n >= lista[0] and n <= lista[1]:
        lista.insert(1, n)
    elif c == 2 and n <= lista[0] and n <= lista[1]:
        lista.insert(0, n)
    elif c == 3 and n >= lista[0] and n <= lista[1] and n <= lista[2]:
        lista.insert(1, n)
    elif c == 3 and n >= lista[0] and n >= lista[1] and n <= lista[2]:
        lista.insert(2, n)
    elif c == 3 and n <= lista[0] and n <= lista[1] and n <= lista[2]:
        lista.insert(0, n)
    elif c == 4 and n >= lista[0] and n <= lista[1] and n <= lista[2] and n <= lista[3]:
        lista.insert(1, n)
    elif c == 4 and n >= lista[0] and n >= lista[1] and n <= lista[2] and n <= lista[3]:
        lista.insert(2, n)
    elif c == 4 and n >= lista[0] and n >= lista[1] and n >= lista[2] and n <= lista[3]:
        lista.insert(3, n)
    elif c == 4 and n <= lista[0] and n <= lista[1] and n <= lista[2] and n <= lista[3]:
        lista.insert(0, n)
print(lista)

# OU