#Empréstimo bancário mensal não pode exceder 30% do valor do salário:
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário atual? '))
anos = int(input('Em quantos anos pretende pagar a dívida? '))

prestaçao = casa / anos
salario30 = (30 / 100 * salario) + salario

if prestaçao <= salario30:
    print('Parabéns! O seu empréstimo bancário foi aprovado!')
else:
    print('Infelizmente o seu empréstimo bancário foi negado!')