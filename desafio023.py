# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:
# Ex.: Digite um número : 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input("Digite um número de 0 a 9999: "))

# ============ 1ª opção ===========
# num = str(numero)
# print(f'Analisando o número {numero}:')
# print(f'Unidade: {num[0]}')
# print(f'Dezena: {num[1]}')
# print(f'Centena: {num[2]} ')
# print(f'Milhar: {num[3]}')

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"===== Analisando o número {numero} =====")
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena} ")
print(f"Milhar: {milhar}")
