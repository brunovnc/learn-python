import math
#Digite o cateto oposto e adjacente e encontre o valor da hipotenusa.
catetooposto = float(input('Qual o valor do cateto oposto?'))
catetoadja = float(input('Qual  o valor do cateto da adjacente?'))

hipotenusa = math.hypot(catetooposto,catetoadja)

print(f'O triângulo retangulo tem {catetooposto} de cateto oposto e {catetoadja} de cateto adjacente resultando em {hipotenusa:.2f} cm')