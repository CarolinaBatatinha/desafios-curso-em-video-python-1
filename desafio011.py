#Fazer um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
lar = float(input('Digite aqui a largura da parede em metros: '))
alt = float(input('Digite aqui a altura da parede em metros: '))

print('A largura da parede é de {:.2f}m e a altura é de {:.2f}m. Sua área é de {}m² e serão necessários {:.2f} litros de tinta pra cobrir toda a área.'.format(lar, alt, lar*alt, (lar*alt)/2))

