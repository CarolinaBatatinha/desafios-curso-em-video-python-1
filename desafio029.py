# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa custará R$ 7,00 por cada Km acima do limite.

vel = int(input('Informe a velocidade registrada em km/h: '))

if vel > 80:
    valor_multa = (vel - 80) * 7
    print('A velocidade registrada foi de {0}km/h.')
    print('Como o limite foi ultrapassado, você pagará uma multa de R$ {0:.2f}.'.format(valor_multa))
else:
    print('A velocidade registrada foi de {0}km/h.'.format(vel))
    print('Continue de olho nos limites das vias.')