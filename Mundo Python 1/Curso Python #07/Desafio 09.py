# Faça um programa que leia o salário do funcionário e depois calcule esse valor com um aumento salarial de 15%.
salario = float(input("Qual é o salário atual do funcionário? R$"))
reajuste = (salario * 15) / 100
salarionovo = salario + reajuste

print(f"O novo salário do funcionário é de R${salarionovo} com um aumento total de R${reajuste}.")