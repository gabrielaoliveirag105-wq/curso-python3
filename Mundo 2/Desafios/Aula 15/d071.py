print('----- DESAFIO 71 ------')
''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

amarelo = '\033[1;33m'
limpa = '\033[m'

notas = 0
nota_atual = 50

print(f'{amarelo} === CAIXA RÁPIDO === {limpa}')
print('Olá, abaixo informe o valor para saque.')

valor = int(input('Informe o valor: R$'))

while True:
    if valor >= nota_atual:
        valor = valor - nota_atual
        notas = notas + 1
    else:
        if notas > 0:
            print(f'Total de {amarelo}{notas}{limpa} cédulas de {amarelo}R${nota_atual}{limpa}')

        if nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 1
        notas = 0
        if valor == 0:
            break
print('-' * 30)
print(f'{amarelo}Saque realizado. Até a próxima!{limpa}')
    
            