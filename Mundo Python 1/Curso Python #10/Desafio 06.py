# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento:
# Para salários superiores a R$1.250,00, calcule um aumento de 10%;
# Para salários inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite o valor do seu salário atual? "))

if salario > 1250:
    valor1 = (10 * salario) / 100
    reajuste1 = salario + valor1
    print(f'O seu novo salário é de R${reajuste1}.') 
else:
    valor2 = (15 * salario) / 100
    reajuste2 = salario + valor2
    print(f'O seu novo salário é de R${reajuste2}.') 