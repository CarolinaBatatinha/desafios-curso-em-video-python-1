#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele
n = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(n))
print('É alfanumérico?',n.isalnum())
print('É um número?',n.isnumeric())
print('Tá em caixa baixa?',n.islower())
print('Tá em caixa alta?',n.isupper())
print('Só tem espaços?',n.isspace())