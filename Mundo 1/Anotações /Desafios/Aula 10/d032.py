print('------- DESAFIO 32 ---------')
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

print('---- ESSE ANO É BISSEXTO? ----')
ano = int(input('Que ano você quer analisar? (Coloque 0 para verificar o ano atual): '))

if (ano == 0):
    ano = date.today().year # Verifica o ano atual conforme a máquina 

if (ano  % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): #Um ano é bissexto se ele for divisível por 4 E NÃO for divisível por 100, A MENOS QUE ele seja divisível por 400.
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')
    