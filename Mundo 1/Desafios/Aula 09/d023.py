print('---------- DESAFIO 23 ----------')
# Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados.
""" Exemplo:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
num = int(input('Digite um valor de 0 a 9999: '))
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10

print(f'Sua unidade é: {u} \nSua dezena é: {d} \nSua centena é: {c} \nSeu milhar é: {m}')

