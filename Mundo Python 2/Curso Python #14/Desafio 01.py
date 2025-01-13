# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça para tentar novamente.
sexo = str(input('Informe o seu sexo (M/F): ')).upper()[0]

while sexo not in 'MmFf':
    print('Não existe essa opção. Tente novamente!')
    sexo = str(input('Informe o seu sexo (M/F): ')).upper()[0]
if sexo == 'M':    
    print('Você é Homem.')
elif sexo == 'F':
    print('Você é Mulher.')