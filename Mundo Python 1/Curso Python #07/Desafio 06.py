# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere: US$1,00 = R$3,27
real = float(input("Quanto você tem na carteira? "))

dolar = 6.18
conversao = real / dolar

print(f"R${real} convertido em dolar fica US${conversao}.")