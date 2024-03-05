pessoas = {'nome':'Bruno', 'sexo':'Masculino', 'idade':'21'}

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'Guanabara' #Para substituir um elemento. Bruno > Guanabara
pessoas['peso'] = 74 #Para adicionar.
del pessoas['sexo'] #Para deletar.
print(pessoas)