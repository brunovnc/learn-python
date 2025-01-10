# Faça um programa que leia o nome de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo de alistamento.
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2025 - ano

if idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos e ainda vai se alistar em {falta} anos.')
elif idade == 18:
    print(f'Você tem {idade} anos e já está na hora de se alistar para o exército!')
else:
    atraso = idade - 18
    print(f'Você tem {idade} anos e seu alistamento passou do prazo há {atraso} anos. Aliste-se urgentemente!')