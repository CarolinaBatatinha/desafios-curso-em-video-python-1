#Criar um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('O número digitado foi {}. \nSeu dobro é igual a {}. \nSeu triplo é igual a {}. \nSua raiz quadrada é igual a {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))