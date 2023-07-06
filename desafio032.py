# Faça um programa que leia um ano qualquer e mostre se o ano é bissexto.

ano = int(input('Digite o ano a ser pesquisado: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('{0} é bissexto.'.format(ano))
else:
    print('{0} não é bissexto'.format(ano))