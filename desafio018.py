#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))


print(f'O seno, cosseno e tangente do ângulo {a} são respectivamente: {s:.2f}, {c:.2f} e {t:.2f} graus.')