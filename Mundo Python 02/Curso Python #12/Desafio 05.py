nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Você reprovou na matéria! Sua média foi {media}, estude mais na próxima!')
elif media > 5.0 and media < 6.9:
    print(f'Você está de recuperação na matéria! Sua média foi {media}.')
else:
    print(f'Parabéns! Sua média foi {media}, você está aprovado!')