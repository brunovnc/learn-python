# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
kmp = float(input("Quantos kilometros foram percorridos? "))
diasalugados = float(input("Poir quantos dias foi alugado? "))
dias = diasalugados * 60
kmpreco = kmp * 0.15
total = dias + kmpreco

print(f"O valor pelos dias alugados foi de R${dias} e pelos kilometros percorridos foi de R${kmpreco} totalizando R${total}.")