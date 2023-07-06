# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu salário atual em R$: '))

if salario <= 1250:
    reajuste = salario * 1.15
else:
    reajuste = salario * 1.1
print('Seu salário reajustado vai para R$ {0:.2f}.'.format(reajuste))