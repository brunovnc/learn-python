n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #Por o número 0 ser considerado par, usamos esse if para desconsiderar o mesmo.
     if n % 2 == 0:
        par = par + 1
     else:
        impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números impares.')