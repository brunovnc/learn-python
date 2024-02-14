frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#O primeiro código diz onde a leitura vai iniciar. Logo, o len(junto) serve para ler a quantidade de caracteres que a palavra junta contém, definindo a última letra da palavra. 
#Ex. 'Calvo' possui 5 letras, logo a última letra é o número 5 (lembrando q a contagem do len começa do 0, logo será len(junto) - 1.)
#O segundo -1 diz aonde a leitura vai parar.
#O último -1 faz com que a leitura ande de trás pra frente
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

print(f'Comparando a frase invertida: {junto, inverso}.')

if junto == inverso:
    print('A frase é um políndromo.')
else:
    print('A frase não é um políndromo.')

#ou sem usar o for:

frase2 = str(input('Digite uma frase: ')).upper().replace(' ', '')

inverso2 = frase2[::-1]

print(f'Comparando a frase invertida: {frase2, inverso2}.')

if frase2 == inverso2:
    print('A frase é um políndromo.')
else:
    print('A frase não é um políndromo.')