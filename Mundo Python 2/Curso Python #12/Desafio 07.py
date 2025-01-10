# Refaça o DESAFIO DO TRIÂNGULO, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# Equilátero: Todos lados iguais;
# Isósceles: Dois lados iguais;
# Escaleno: Todos os lados diferentes.
l1 = int(input('Digite o valor de um lado do triângulo em cm: '))
l2 = int(input('Digite o valor outro lado do triângulo em cm: '))
l3 = int(input('Digite o valor mais outro lado do triângulo em cm: '))

if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1 or l1 == l2 == l3:
    print('É possível formar um triângulo com esses valores.')
    if l1 == l2 == l3:
        print('Todos os lados são iguais, logo é um triângulo Equilátero.')
    elif l1 == l2 and l1 != l3:
        print('Os dois lados são iguais, logo é um triângulo Isósceles.')
    elif l1 == l3 and l1 != l2:
        print('Os dois lados são iguais, logo um triângulo Isósceles.')
    elif l1 != l2 != l3:
        print('Todos os lados são diferentes, logo é um triângulo Escaleno.')
else:
    print('Não é possível formar um triângulo com esses valores.')
