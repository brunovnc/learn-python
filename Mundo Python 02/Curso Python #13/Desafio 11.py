somaidade = 0
média = 0
velho = 0
nomevelho = ''
mulher20 = 0

for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: '))
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 = mulher20 + 1
#Se "p1" e "sexo" seja masculino: velho = idade e nomevelho = nome. (Testando se o primeiro indivíduo é o mais velho).
#Caso contrário, se em "sexo" seja masculino e idade maior que velho (o primeiro indivíduo), então velho = idade e nomevelho = nome.
#Se em "sexo" seja feminino e idade menor que 20: Acrescenta 1 em "mulher20".

média = somaidade / 4
print(f'A média de idade do grupo é de {média} anos.')
print(f'O homem mais velho tem {velho} e se chama {nomevelho}.')
print(f'No total existem {mulher20} mulheres com menos de 20 anos.')