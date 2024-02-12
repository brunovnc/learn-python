#Fatiamento: para selecionar um caracter de uma string:
frase = 'Frase do dia'
print(frase[1])
#ou para selecionar mais de um caracter:
print(frase[0:5])
#ou pra pular caracteres:
print(frase[0:11:3])
#ou a mesma coisa que 0:5:
print(frase[:5])
#ou
print(frase[9:])
#ou pra pular caracteres também:
print(frase[0::2])
#Quando omitimos o valor inicial, ele reconhece a primeira letra no inicio e o mesmo vale pro valor final. Ex. :3 ou 5: ou 4::3.

#Analise: saber algumas informações sobre a string.
#Contar cada casa de palavras:
print(len(frase))
#Contar quantas vezes aparece uma letra:
print(frase.count('a'))
#ou utilizando Fatiamento:
print(frase.count('a', 0, 5))
#Onde encontrou um ou mais caracteres específicos:
print(frase.find('ase'))
#Se existe uma palavra específica na string:
print('dia' in frase)

#Transformação:
#Para substituir uma palavra ou caracter:
print(frase.replace('dia', 'day'))
#Para tornar as letras maiúsculas:
print(frase.upper())
#Para tornar as letras minúsculas:
print(frase.lower())
#Para tornar as letras minúsculas porém a letra inicial continuará maiúscula:
print(frase.capitalize())
#Para tornar as letras minúsculas e somente a letra inicial maiúscula de partes específicas onde há espaço entre palavaras da string:
print(frase.title())
#Para remover espaços inúteis no início ou fim de uma string:
print(frase.strip())

#Divisão:
#Criar uma divisão dentro do espaço de uma string:
print(frase.split())

#Junção:
#Juntar um caracter em espaços de uma string:
print('-'.join(frase))

#EXEMPLOS EXTRAS COMBINAÇÕES:
print(frase.upper().count('a'))
#outro exemplo:
teste = 'Curso em Vídeo Python'
dividido = teste.split()
print(dividido[3])
#mais
dividido = teste.split()
print(dividido[3][2])