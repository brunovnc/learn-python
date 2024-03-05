documentos = dict() #dicionário

documentos['Nome'] = str(input('Nome: '))
documentos['Sexo'] = str(input('Sexo: ')).upper()
documentos['Nascimento'] = int(input('Ano de nascimento: '))
documentos['CTPS'] = int(input('CTPS: (0 = NÃO POSSUI) '))
documentos['Idade'] = 2024 - documentos['Nascimento']

if documentos['CTPS'] != 0:
    documentos['Contratação'] = int(input('Ano de contratação: '))
    documentos['Salario'] = float(input('Salário: R$'))
    if documentos['Sexo'] == 'MASCULINO':
        documentos['Aposentadoria'] = documentos['Idade'] + (documentos['Contratação'] + 35) - 2024 #35 anos de colaboração
    if documentos['Sexo'] == 'FEMININO':
        documentos['Aposentadoria'] = documentos['Idade'] + (documentos['Contratação'] + 30) - 2024 #30 anos de colaboração

print('=-'*15)
print('           DADOS:')
print('=-'*15)
for k, v in documentos.items():
    print(f'  - {k} = {v}')