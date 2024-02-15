while True:
    sexo = input('Digite o seu sexo: [M/F] ')
    if sexo == 'M' or sexo == 'F':
        break
if sexo == 'M':
    sexo = 'Masculino'
if sexo == 'F':
    sexo = 'Feminino'
print(f'Sexo {sexo} registrado com sucesso!')

#ou

sexo2 = str(input('Digite o seu sexo: [M/F] ')).upper() [0]

while sexo2 not in "MmFf":
    sexo2 = str(input('Dados invalidos. Por gentileza. digite o seu sexo: [M/F] '))
if sexo2 == 'M':
    sexo2 = 'Masculino'
if sexo2 == 'F':
    sexo2 = 'Feminino'
print(f'Sexo {sexo2} registrado com sucesso!')