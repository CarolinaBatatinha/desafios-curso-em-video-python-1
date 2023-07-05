# Faça um programa que leia uma frase pelo teclado e mostre:
# a) quantas vezes aparece a letra "A";
# b) em que posição ela aparece a primeira vez;
# c) em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {0} vezes na frase.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {0}.'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {0}.'.format(frase.rfind('A')+1))