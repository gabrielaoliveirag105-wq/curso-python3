print('----- DESAFIO 59 ------')
'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
print(' --- MENU INTELIGENTE DE VALORES ---')
n1 = int(input('Escolha o primeiro valor: '))
n2 = int(input('Escolha o segundo valor: '))
sleep(1)

c = 0
maior = 0 
opcao = 0

while opcao != 5:
    print('\n|    MENU INTELIGENTE    | '
    '\n-------------------------|'
    '\n| [1] Soma               | '
    '\n| [2] Multiplicar        | '
    '\n| [3] Maior              | '
    '\n| [4] Novos números      | '
    '\n| [5] Sair do programa   | '
    '\n|------------------------|')
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma do valor {n1} com {n2} é igual a {soma}.')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O produto da multiplicação de {n1} com {n2} é igual a {mult}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O número maior entre {n1} e {n2} é o {maior}.')
        elif n2 > n1:
            maior = n2
            print(f'O número maior entre {n1} e {n2} é o {maior}.')
        else:
            print('Os dois valores são iguais')
    elif opcao == 4:
        print('\033[1;34mInforme os novos valores...\033[m')
        n1 = int(input('Escolha o primeiro valor: '))
        n2 = int(input('Escolha o segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa...')
    else:
        print('\033[4;31mOpção Inválida. Tente novamente!\033[m')
print('\033[1;33mFim do Menu Inteligente. Até a próxima.\033[m')

