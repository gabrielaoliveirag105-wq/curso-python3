print('------ DESAFIO 10 ------') 
# Faça um programa que leia quantos reias uma pessoa tem, e quantos dólares ela consegue comprar.

reais = float(input('Informe o valor em reais que você possui: R$ '))
dolar =  reais / 3.27 # valor digitado pelo usuario dividido pela cotação para descobrir o valor.
print(f'Com R$ {reais} você consegue comprar US$ {dolar:.2f}')