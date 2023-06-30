#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('A primeira nota foi {}, a segunda nota foi {} e sua média é de {:.2f}.'.format(n1, n2, (n1+n2)/2))