print('=-'*20)
print('Calculadora Índice de Massa Corporal:')
print('=-'*20)

peso = float(input('Qual o seu peso atual? '))
altura = float(input('Qual a sua altura em metros? '))

imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} kg/m². Está classificado abaixo do peso.')
elif imc >= 18.5 and imc < 25.0:
    print(f'Seu IMC é {imc:.2f} kg/m². Você está com o peso ideal.')
elif imc >= 25.0 and imc < 30.0:
    print(f'Seu IMC é {imc:.2f} kg/m². Está classificado em Sobrepeso.')
elif imc >=30.0 and imc <40:
    print(f'Seu IMC é {imc:.2f} kg/m². Está classificado em Obesidade.')
elif imc >= 40.0:
    print(f'Seu IMC é {imc:.2f} kg/m². Cuidado! Está classificado em Obesidade Mórbida.')