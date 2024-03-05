#Lista com dicionários.
brasil = [] #Lista
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'} #dicionario
estado2 = {'uf':'São Paulo', 'sigla':'SP'} #dicionario
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1])
print(brasil[0]['uf'])