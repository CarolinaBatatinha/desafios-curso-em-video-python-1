#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre a hipotenusa.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)


print('A hipotenusa vai medir {:.2f} graus'.format(hi))

#OU
#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float (input('Comprimento do cateto adjacente: '))

#hi = math.hypot(co, ca)
