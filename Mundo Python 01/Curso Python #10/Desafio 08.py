#Leia 3 comprimentos de retas e informe se é possível formar um triângulo com as mesmas:

print('-='*20)
print('Analisador de Triângulos:')
print('-='*20)

lado1 = float(input('Digite o valor do primeiro lado:'))
lado2 = float(input('Digite o valor do segundo lado:'))
lado3 = float(input('Digite o valor do terceiro lado:'))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado2:
    print("Não é possível formar um triângulo!")
elif lado1 == lado2 and lado1 == lado3:
    print("Este triangulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3:
    print("Este triangulo é Isósceles.")
else:
    print("Este triangulo é Escaleno.")

#Sempre que a soma das medidas dos segmentos que estão sendo girados for maior que a medida do terceiro segmento, é possível construir um triângulo.