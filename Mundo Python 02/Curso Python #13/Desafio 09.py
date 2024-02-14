#2006 = 18 anos
for c in range(0, 7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = 2024 - nascimento
    faltaidade = nascimento - 2006
    if nascimento < 2006:
        print(f'Você tem {idade} anos e consequentemente é maior de idade.')
    else:
        print(f'Você tem {idade} anos e consequentemente é menor de idade. Faltam {faltaidade} anos para completar os 18 anos.')