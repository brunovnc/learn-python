# Refaça o DESAFIO DA TABUADA, mostrando a tabuada de um número que o usuário escolher, porém, usando o Laço de Repetição For.
n = int(input('Digite um número de 0 a 10 para a tabuada: '))

for c in range(0, 11):
    print(f'{n} x {c} = {n * c}')
print('FIM!')