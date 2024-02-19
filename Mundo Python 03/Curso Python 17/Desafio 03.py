lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Primeiro valor e último valor.
        lista.append(n)
    else:
        posiçao = 0
        while posiçao < len(lista): #Repetir da menor posição até total de posição da lista:
            if n <= lista[posiçao]: #Se n for menor ou igual ao valor da posição da lista inserir n na posição.
                lista.insert(posiçao, n)
                break
            posiçao += 1 #Posição andar conforme o laço se repita.
print(lista)
print('Desafio encerrado.')