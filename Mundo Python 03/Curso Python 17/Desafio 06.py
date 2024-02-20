exp = str(input('Digite uma expressão numérica: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
#Em resumo, toda vez que o programa encontrar '(', ele vai acrescentar +1'(' em pilha.
#Porém, toda vez que o programa encontrar ')', ele vai remover o '(' que foi acrescentado anteriormente.
#Com isso, se a len(pilha) == 0, significa que a pilha está válida, pois teoricamente não irá conter nada na lista pilha.
if len(pilha) == 0:
    print('Sua expressão numérica está válida.')
else:
    print('Sua expressão numérica está errada.')