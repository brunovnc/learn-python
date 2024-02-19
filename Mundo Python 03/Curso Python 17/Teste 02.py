valores = list() #Outra opção de usar lista.

for contador in range(0, 5): #Vão ser adicionados valores pelo input.
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')