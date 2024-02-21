teste = []
teste.append('Bruno')
teste.append(40)

galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

###

galeraa = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galeraa[0])
print(galeraa[0][0])
print(galeraa[2][0])