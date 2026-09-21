print('----- DESAFIO 57 ------')

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from time import sleep

c = 0

print(' --- VALIDAÇÃO DE DADOS --- ')
print('Olá, seja bem-vindo (a), vamos validar seus dados')
sleep(1)

nome = str(input('\nDigite seu nome: '))
idade = int(input('Digite sua idade: '))
sexo = str(input('Informe seu sexo: [F/M] ')).upper()

while sexo not in ['F', 'M']:
    print('\033[1;31mOpção Inválida. Tente novamente!\033[m')
    sexo = str(input('Informe seu sexo: [F/M] ')).upper()
    c = c + 1

sleep(1)
print('\n\033[4;33mColetando dados...\033[m')
sleep(1)
print(f'\n\033[1;32m{nome}, seus dados foram coletados! Programa finalizado.\033[m')


        