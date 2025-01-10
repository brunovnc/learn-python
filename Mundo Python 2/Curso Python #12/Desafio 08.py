# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade:
# Acima de 30: Obesidade mórbida.
peso = float(input('Digite o seu peso atual em Kg: '))
altura = float(input('Digite a sua altura em M: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'DESNUTRIÇÃO. Seu IMC é no valor de {imc:.1f}.')
elif imc >= 18.5 and imc < 25:
    print(f'PESO IDEAL. Seu IMC é no valor de {imc:.1f}.')
elif imc >= 25 and imc < 30:
    print(f'SOBREPESO. Seu IMC é no valor de {imc:.1f}.')
elif imc >= 30 and imc < 40:
    print(f'OBESIDADE. Seu IMC é no valor de {imc:.1f}.')
else:
    print(f'OBESIDADE MÓRBIDA. Seu IMC é no valor de {imc:.1f}.')