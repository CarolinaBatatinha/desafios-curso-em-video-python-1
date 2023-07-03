#Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite um valor em metros: '))
print('O valor em metros é igual a {}m. \nEm centímetros, o valor passa para {}cm. \nEm milímetros, o valor é de {}mm.'.format(n, (n*100), (n*1000)))
