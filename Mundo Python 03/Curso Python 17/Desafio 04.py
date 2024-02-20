lista = []
contador = 0

while True:
    n = int(input('Digite um valor: '))
    contador += 1
    if n == 5 and 5 not in lista:
        print('O número 5 não estava na lista mas foi adicionado.')
    elif n == 5 and 5 in lista:
        print('O número 5 já estava na lista mas foi adicionado mais uma vez.')
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(n)
    if continuar == 'N':
        break
print(f'No total foram digitados: {contador} números.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem decrescente ficou: {lista}.')
        