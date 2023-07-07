#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float (input('Quantos km o cliente rodou com o veículo? '))
dias = float (input('Por quantos dias o veículo foi alugado? '))

diaria = 60
km_rodado = 0.15 * km 
total = (diaria * dias) + (km_rodado)

print('O valor a pagar é de R${:.2f}.'.format(total))