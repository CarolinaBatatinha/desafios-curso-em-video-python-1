#O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do primeiro aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem da apresentação será: ',(lista))
