valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
#ou de forma mais bonita:
for v in valores: #Para cada valor em valores print...
    print(f'{v}...', end='')
#ou
for p, v in enumerate(valores):
    print(f'\nNa posição {p} encontrei o valor {v}.')
print('Cheguei ao final da lista.')