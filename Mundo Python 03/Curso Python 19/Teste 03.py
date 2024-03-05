estado = {} #dicionário
brasil = [] #lista

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #Funciona para copiar uma lista da mesma maneira do [:], porém utilizado nos dicionários.

for e in brasil: #Para cada estado em brasil...
    for k, v in e.items(): #Para mostrar de forma bonita cada item: Para cada key, valor em estado...
        print(f'O campo {k} tem valor {v}.')
#ou
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print() #pra pular linha
