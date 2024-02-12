salario = float(input('Digite o valor atual do seu salário:'))

if salario >1250.0:
    salarionovo = (10/100 * salario) + salario
    aumento = salarionovo - salario
    print(f'O seu novo salário será de R${salarionovo} recebendo um aumento de R${aumento}')
else:
    salarionovoo = (15/100 * salario) + salario
    aumentoo = salarionovoo - salario
    print(f'O seu novo salário será de R${salarionovoo} recebendo um aumento de R${aumentoo}')