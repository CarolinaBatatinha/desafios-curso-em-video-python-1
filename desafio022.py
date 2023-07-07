# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas;
# - o nome com todas as letras minúsculas;
# - quantas letras no total, sem considerar espaços;
# - quantas letras tem o primeiro nome.

nome_completo = input('Digite seu nome completo: ')
letras_maiusculas = nome_completo.upper()
letras_minusculas = nome_completo.lower()
total_letras = len(nome_completo) - nome_completo.count(' ') #subtrai os "espaços" do nome completo
total_letras_primeiro_nome = nome_completo.find(' ') #porque o primeiro nome termina no primeiro espaço
nome_separado = nome_completo.split()

print(f'''
- Nome completo com todas as letras maiusculas: {letras_maiusculas}
- Nome completo com todas as letras minusculas: {letras_minusculas}
- Total de letras, sem considerar espacamento: {total_letras}
- Total de letras do nome {nome_separado[0]}: {total_letras_primeiro_nome}''')
