# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da cidade: ')).lower()
divisor = cidade.split()

print(divisor[0].find('santo'))