# While = Enquanto
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

print('---------------------------')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

print('---------------------------')

s = 1
par = impar = 0
while s != 0:
    s = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} número e {impar} números impares!')