salario = float(input('Qual o seu salário atual?'))
#Funcionário recebeu 15% de acrescimo salarial. Calcule:
acrescimo = 15 / 100 * salario
salarionovo = salario + acrescimo

print(f'O seu novo salário será de R${salarionovo} recebendo um acrescimo salarial de R${acrescimo:.2f}.')