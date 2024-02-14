#Para evitar fazer o mesmo comando várias vezes aumentando o tempo de trabalho, utilizamos a estrutura de repetição FOR:

for c in range(0, 6):
    print('Oi')
print('Fim.')

#ou se quiser repetir mais de um:

for c in range(0, 6):
    print('Oi')
    print('Olá')
print('Fim.')

#ou se quiser repetir do fim para o início:

for c in range(6, 0, -1):
    print(c)
print('Fim.')

#ou pulando de 2 em 2:

for c in range(0, 6, 2):
    print(c)
print('Fim.')