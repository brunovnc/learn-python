#Leia um nome completo com letras maisculas, minusculas, contar a quantidade de letras sem o espaço e contar a quantidade de letras do primeiro nome:
nome = input('Digite o seu nome completo:') .strip()

maiuscula = nome.upper()
print(maiuscula)

minuscula = nome.lower()
print(minuscula)

letrastotal = nome.strip()
print(len(letrastotal) - letrastotal.count(' '))
#Removemos os espaços desnecessários do início e do final (strip), depois contamos o total de caracteres do nome (len) - o total da contagem de caracteres do comando (count),
#que no caso foi o espaço.

primeironome = nome.split()
print(len(primeironome[0]))