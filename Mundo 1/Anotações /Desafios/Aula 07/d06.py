print('------ DESAFIO 06 ------') 
# Crie um programa que leia um núemro e mostre seu dobro, seu triplo e sua raiz quadrada.

num = int(input('Escolha um número: ' ))
d = num * 2
t = num * 3
raiz = num ** (1/2)

print(f'O dobro de {num} vale {d}. \nJá o triplo de {num} vale {t}. \nE a Raiz Quadrada de {num} vale {raiz:.2f}. ')