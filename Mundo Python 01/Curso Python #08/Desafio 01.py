import math
#Digite um número quebrado e mostre seu número inteiro. Ex. 6.127 = 6
numeroreal = float(input('Digite um número real:'))

parteinteira = math.floor(numeroreal)

print(f'A parte inteira de {numeroreal} é {parteinteira}')