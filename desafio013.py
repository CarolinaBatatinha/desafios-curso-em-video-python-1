#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input("Digite o seu último salário: R$ "))
print('Seu último salário foi de R${:.2f}, mas no próximo mês você passará a receber R${:.2f}.'.format(sal, (sal+(sal*15)/100)))