print(' ----- DESAFIO 72 ----- ')
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
print(' ---- ESCREVENDO NÚMEROS POR EXTENSO ----')

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
           'cinco', 'seis', 'sete', 'oito', 'nove', 
           'dez', 'onze', 'doze', 'treze', 'quatorze', 
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 
           'dezenove', 'vinte')


while True:
    while True: 
        num  = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('\033[1;31mNúmero inválido! Tente novamente.\033[m')

    print(f'Você digitou o número \033[1;33m{extenso[num]}\033[m')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    if resp == 'N':
        break
print('Programa encerrado! Até a próxima.')
