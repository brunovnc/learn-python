lista = list()
media = list()

print('=-'*20)
print('          BOLETIM ACADÊMICO:')
print('=-'*20)

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('1° Nota: ')))
    lista.append(float(input('2° Nota: ')))
    mediaaluno = (lista[1] + lista[2]) / 2
    lista.append(mediaaluno)
    media.append(lista[:])
    lista.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('=-'*20)

print('No. NOME          MÉDIA')
for c, n in enumerate(media):
    print(f'{c:<4}{n[0]:<10}{n[3]:>8.1f}')

while True:
    print('-'*25)
    mostrar = int(input('Mostrar notas de qual aluno? (999 BREAK) '))
    for c, n in enumerate(media):
        if mostrar == c:
            print(f'As notas de {n[0]} foram: {n[1]} e {n[2]}.')
    if mostrar == 999:
        break


