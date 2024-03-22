def somar(a= 0, b=0, c=0):
    s = a + b + c
    return s #Ao invés de printar "A soma vale 10", "A soma vale 8", "A soma vale 4" repetitivamente.
             #É possível retornar tudo de uma vez só.

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')