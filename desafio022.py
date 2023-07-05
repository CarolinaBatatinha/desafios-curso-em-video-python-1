# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas;
# - o nome com todas as letras minúsculas;
# - quantas letras no total, sem considerar espaços;
# - quantas letras tem o primeiro nome.

nomeCompleto = input('Digite seu nome completo: ')
letrasMaiusculas = nomeCompleto.upper()
letrasMinusculas = nomeCompleto.lower()
totalLetras = len(nomeCompleto) - nomeCompleto.count(' ') #subtrai os "espaços" do nome completo
totalLetrasPrimeiroNome = nomeCompleto.find(' ') #porque o primeiro nome termina no primeiro espaço
nomeSeparado = nomeCompleto.split()

print(f'''
- Nome completo com todas as letras maiusculas: {letrasMaiusculas}
- Nome completo com todas as letras minusculas: {letrasMinusculas}
- Total de letras, sem considerar espacamento: {totalLetras}
- Total de letras do nome {nomeSeparado[0]}: {totalLetrasPrimeiroNome}''')
