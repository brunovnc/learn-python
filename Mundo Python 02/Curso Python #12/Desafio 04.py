ano = int(input('Qual o ano do seu nascimento?'))

falta = ano - 2006
passou = 2006 - ano

alistamento = input('Você já se alistou ao serviço militar? ')
if ano == 2006 and alistamento in 'Não não Nao Não':
    print('Está na hora de se alistar ao serviço militar!')
elif ano > 2006:
    print(f'Você ainda é menor de 18 anos. Faltam {falta} anos para se alistar ao serviço militar!')
elif ano < 2006 and alistamento in 'Não não Nao Não':
    print(f'Já passou do tempo de servir às forças armadas! Passaram {passou} anos de vencimento. Aliste-se urgentemente!')
else:
    print('Seu compromisso com as forças armadas está em dia! Seus direitos estão garantidos!')