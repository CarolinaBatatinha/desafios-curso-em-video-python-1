# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

num_computador = randint(0,5)
num_usuario = int(input('Digite um número inteiro entre 0 e 5: '))

if num_usuario == num_computador:
    print('Parabéns, você acertou o número sorteado.')
else:
    print(f'Você escolheu {num_usuario} e o computador escolheu {num_computador}.')
