# Crie um programa que tenha uma tupla com várias palavras. Depois mostre para cada palavra quais são as vogais.
palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar')

for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos: ', end='')
    if 'a' in palavras[c]:
        print(f'a', end='')
    if 'e' in palavras[c]:
        print(f' e', end='')
    if 'i' in palavras[c]:
        print(f' i', end='')
    if 'o' in palavras[c]:
        print(f' o', end='')
    if 'u' in palavras[c]:
        print(f' u', end='')

# OU
print('\n-',
      '\nOU'
      '\n-')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')