# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input("Digite o preço do produto: "))
desconto = (5 * preco) / 100
precofinal = preco - desconto

print(f"O preço do produto com o desconto de 5% é de R${precofinal}.")