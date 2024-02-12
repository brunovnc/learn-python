print('=-'*20)
print('Confederação Nacional de Natação:')
print('=-'*20)

ano = int(input('Digite o ano do seu nascimento: '))
#2006 = 18 anos

if ano >= 2015:
    print('Sua categoria é: Mirim.')
elif ano < 2015 and ano >= 2010:
    print('Sua categoria é: Infantil.')
elif ano < 2010 and ano >= 2005:
    print('Sua categoria é: Junior.')
elif ano < 2005 and ano >= 2004:
    print('Sua categoria é: Sênior.')
elif ano < 2004:
    print('Sua categoria é: Master.')
