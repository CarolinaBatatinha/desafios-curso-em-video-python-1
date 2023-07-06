# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 por km para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem em km: '))

if distancia <= 200:
    valorPassagem = distancia * .5
    print('Para uma viagem de {0}km, o valor da passagem é de R$ {1:.2f}.'.format(distancia, valorPassagem))
else:
    valorPassagem = distancia * .45
    print('Para uma viagem de {0}km, o valor da passagem é de R$ {1:.2f}.'.format(distancia, valorPassagem))

#TAMBÉM SERIA POSSÍVEL SUBSTITUIR COMPLETAMENTE O "if-else" PELA CONDIÇÃO ABAIXO

#valorPassagem = distancia * .5 if distância <= 200 else distancia * .45
