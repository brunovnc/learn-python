#se significa 'if' / se não significa 'else' e agora temos o 'elif' se não se:
nome = str(input('Qual é o seu nome? '))

if nome == 'Bruno':
    print(f'Que nome lindo!')

elif nome in 'Mayke Gustavo Devinho':
    print(f'Que nome de jogador de League of Legends! Sorye Ge Ton, {nome}.')

elif nome == 'Soares':
    print(f'Senti o cheiro de cú não virgem daqui!')

else:
    print(f'Tenha um bom dia {nome}!')

print('Tenha um bom dia!')