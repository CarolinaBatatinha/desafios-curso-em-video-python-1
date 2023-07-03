#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
#Considerar US$1,00 = R$ 3,27
din = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Você tem R${:.2f} e, com essa grana, você consegue comprar US${:.2f}.'.format(din,(din/3.27)))