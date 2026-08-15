print('----- DESAFIO 15 -------\n')
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

print('------- ALUGUEL DE CARROS ---------')
distancia = float(input('Quantos Km foram percorridos? '))
dias = int(input('Esse carro foi alugado por quantos dias? '))
total = (dias * 60) + (distancia * 0.15)

print(f'Esse carro percorreu {distancia:.1f}Km em {dias} dias, o valor a pagar é de: R$ {total:.2f}')