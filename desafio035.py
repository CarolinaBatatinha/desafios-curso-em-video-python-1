# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = int(input('Informe o comprimento da primeira reta: '))
reta2 = int(input('Informe o comprimento da segunda reta: '))
reta3 = int(input('Informe o comprimento da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta3 + reta2) > reta1:
    print('É possível formar um triângulo com as medidas informadas.')
else:
    print('Não é possível formar um triângulo com as medidas informadas.')