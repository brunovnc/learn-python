# TIPOS PRIMITIVOS E SAÍDA DE DADOS:
n = input('Digite alguma coisa: ')

print(n.isalpha())
# isalpha significa se a variavel em questão (n) é um alfabeto ou não.

print(n.isnumeric())
# isnumeric significa se a variavel em questão (n) é númerica ou não.

print(n.isalnum())
# isalnum significa se a variavel em questão (n) é uma letra ou número ou não.

print(n.isupper())
# isupper significa se a variavel em questão (n) é maiúsculo ou não.

print(n.islower())
# islower significa se a variavel em questão (n) é minúscula ou não.

print(n.istitle())
# istitle siginifica se a variável em questão (n) tem letras maiúsculas e minúsculas ao mesmo tempo.

print(n.isspace())
# istitle siginifica se a variável em questão (n) somente tem espaços.

print(n.__class__)
# __class__ siginifica se a variável em questão (n) é uma str, float, bool ou int.