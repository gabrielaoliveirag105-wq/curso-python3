print('----- DESAFIO 44 ------')
"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros"""

from time import sleep
print('----- CÁLCULO DE PAGAMENTO ------')
valor = float(input('Digite o valor do produto: R$ '))

print('Condições de pagamento: '
'\n----------------------------------------------'
'\n|1 - Á vista dinheiro/cheque: 10% de desconto|' 
'\n|2 - Á vista no cartão: 5% de desconto       |'      
'\n|3 - Em até 2x no cartão: preço formal       |'      
'\n|4 - 3x ou mais no cartão: 20% de juros      |'  
'\n----------------------------------------------'     
'\n')

opcao = int(input('Digite a condição de pagamento desejada: '))
sleep(1)

if opcao == 1:
    desconto = valor * (10/100)
    valor_final = valor - desconto
    print(f'Com 10% de desconto, o produto que custava R$ {valor:.2f}, passa à custar R$ {valor_final:.2f}.')
elif opcao == 2:
    desconto = valor * (5/100)
    valor_final = valor - desconto
    print(f'Com 5% de desconto, o produto que custava R$ {valor:.2f}, passa à custar R$ {valor_final:.2f}.')
elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${valor/2:.2f}, o \nproduto sai pelo preço formal de R$ {valor:.2f}, sem juros.')
elif opcao == 4:
    juros = valor *(20/100)
    valor_final = valor + juros
    dividir = int(input('Em quantas vezes você deseja parcelar? '))
    print(f'Sua compra será parcelada em {dividir}x de R${valor_final/dividir:.2f} ')
    print(f'Com 20% de juros, o produto que custava R$ {valor:.2f}, passa à custar R$ {valor_final:.2f}.')
else:
    print('\033[4;31mOpção Inválida. Tente novamente.\033[m')
