#Leia o nome de cidades e diga se ela começa ou não com a palavra "SANTO":
cidade = input('Digite o nome de uma cidade:').lower().split()

print('santo' in cidade[0])
