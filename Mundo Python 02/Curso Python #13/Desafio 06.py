#Progressão aritmétrica:

primeirotermo = int(input('Digite o valor do primeiro termo aritmétrico: '))
razão = int(input('Digite o valor da razão aritmétrica: '))

for c in range(0,10):
    progressão = primeirotermo + razão * c
    print(progressão, end='->')