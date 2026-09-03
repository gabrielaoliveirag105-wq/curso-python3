print('----- DESAFIO 36 ------')
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
print('\033[4;31m------ EMPRÉSTIMO BANCÁRIO ------\033[m')
sleep(1)

nome = str(input('Olá, qual é o seu nome? '))
casa = float(input(f'{nome}, digite o valor da casa que deseja comprar: R$ '))
sal = float(input('Por favor, informe o seu salário: R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))

print('-'*40)
print('Calculando resultado...')
sleep(1)

prestacao = casa / (anos * 12)

if prestacao > (sal * 30/100):
    print(f'{nome}, infelizmente o seu empréstimo foi negado, pois a prestação mensal de R$ {prestacao:.2f} excede 30% do seu salário')
else:
    print(f'Parabéns {nome}, o seu empréstimo foi aprovado! \nA prestação mensal será de R$ {prestacao:.2f}')