a = [2, 3, 4, 7]
b = a
b[2] = 8 #Quando colocamos que b=a não criamos uma cópia de "a" 
#mas sim interligamos um ao outro, se mudar um, muda o outro.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Para criar a cópia de uma lista usa-se [:].
c = [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(f'Lista C: {c}')
print(f'Lista D: {d}')