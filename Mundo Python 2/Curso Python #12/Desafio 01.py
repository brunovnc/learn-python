# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = float(input('Em quantos anos pretende pagar? '))

mes = tempo * 12
prestacaomensal = casa / mes
salario30 = (salario * 30) / 100

if prestacaomensal < salario30:
    print(f'Parabéns! O seu empréstimo bancário foi aprovado!\n A prestação mensal será no valor de R${prestacaomensal}.')
else:
    print('Infelizmente o seu empréstimo bancário foi recusado.')