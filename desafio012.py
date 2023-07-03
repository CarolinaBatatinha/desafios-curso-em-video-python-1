#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite aqui o preço do produto: R$ '))
print('O preço desse produto é de R${:.2f}\nCom o desconto de 5%, o produto passa a valer R${:.2f}.'.format(preco, (preco - (preco*5/100))))