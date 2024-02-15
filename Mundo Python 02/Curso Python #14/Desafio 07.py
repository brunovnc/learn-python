elementos = int(input('Quantos elementos você quer na Sequência de Fibonaci? '))

n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='') #Na sequência de Fibonacci o 0 e 1 são padrão de início então deixamos o n1=0 e n2=1.

contador = 3 #Contador vai iniciar com 3 pois n3 já está nesse valor por porconta da soma do n1+n2.
while contador <= elementos: #Se o contador for maior que a quantidade de elementos resultará no Break.
    n3 = n1 + n2
    print(f' -> {n3}' , end='')
    contador += 1
    n1 = n2 #A lógica aqui é que vou estar passando o n1 pra casa do n2 assim obtendo uma nova soma.
    n2 = n3 #No mesmo caso daqui (Exemplo no final)
print(f' -> Fim.')

#0 - 1 - 1  ->>  0 - 1 - 1 - 2 - 3 - 5          Ou seja, o n1 e n2 pularam de casa e a soma entre eles resultaram no n3.
#n1  n2  n3  ->>    n1   n2  n3