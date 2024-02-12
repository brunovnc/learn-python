preço = float(input('Qual o preço atual do produto?'))
#Calcular desconto de 5% do produto:
desconto = (5 / 100) * preço
preçodescontado = preço - desconto

print(f'Com o desconto de 5% o produto sai custando R${preçodescontado} recebendo um desconto de R${desconto:.2f}.')