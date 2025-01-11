# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro/cheque: 10% de desconto;
# 1x no cartão: 5% de desconto;
# 2x no cartão: Preço normal;
# 3x ou mais no cartão: 20% de juros.
preco = float(input('Digite o preço do produto: R$'))
pagamento = int(input('1 - Á vista Dinheiro/Cheque: 10% de desconto \n2 - 1x Cartão: 5% de desconto \n3 - 2x Cartão: Preço padrão \n4 - 3x ou + no Cartão: 20% de juros \nQual o método de pagamento? Escolha a opção 1, 2, 3 ou 4: '))

if pagamento == 1:
    avista = (preco * 10) / 100
    precoavista = preco - avista
    print(f'O preço do produto Á VISTA está no valor de R${precoavista}. Desconto de R${avista}.')
elif pagamento == 2:
    cartao1x = (preco * 5) / 100
    precocartao1x = preco - cartao1x
    print(f'O preço do produto á vista 1X CARTÃO está no valor de R${precocartao1x}. Desconto de R${cartao1x}.')
elif pagamento == 3:
    print(f'O preço do produto parcelado em 2x CARTÃO está no valor de R${preco}. Não há desconto parcelando em 2x no cartão.')
elif pagamento == 4:
    cartao3x = (preco * 20) / 100
    precocartao3x = preco + cartao3x
    print(f'O preço do produto parcelado em 3x OU + CARTÃO está no valor de R${precocartao3x}. Juros de R${cartao3}.')
else:
    print('Essa opção não existe! Tente novamente.')