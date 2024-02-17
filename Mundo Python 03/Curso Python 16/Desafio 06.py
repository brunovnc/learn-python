palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for vogais in palavras:
    print(f'\nNa palavra {vogais.upper()} temos a vogal: ', end='')
    for letra in vogais:
        if letra in 'aeiou':
            print(letra, end=' ')