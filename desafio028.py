# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

numComputador = randint(0,5)
numUsuario = int(input('Digite um número inteiro entre 0 e 5: '))

if numUsuario == numComputador:
    print('Parabéns, você acertou o número sorteado.')
else:
    print(f'Você escolheu {numUsuario} e o computador escolheu {numComputador}.')
