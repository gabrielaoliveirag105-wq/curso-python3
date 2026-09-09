print('----- DESAFIO 53 ------')
"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

vermelho = '\033[4;31m'
verde = '\033[4;32m'
limpa = '\033[m'

print(f'{verde}=== ANÁLISE DE PALÍNDROMO === {limpa}')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''

for letra in range(len(junto) - 1, -1, -1):
    invertido += junto[letra]
if invertido == junto:
    print(f'A frase {verde}-{frase}- é {limpa} um {verde}palíndromo!{limpa}')
else:
    print(f'A frase {vermelho}-{frase}- não{limpa} é um {vermelho}palíndromo!{limpa}')
