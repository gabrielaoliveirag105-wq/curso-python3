print('----- DESAFIO 54 ------')
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

vermelho = '\033[4;31m'
verde = '\033[4;32m'
limpa = '\033[m'

print(f'{vermelho}=== ANALISANDO NASCIMENTO ==={limpa}')
from datetime import date

tot_s = 0
tot_n = 0
for c in range(1,8):
    nasc = int(input(f'Informe o ano de nascimento da {c}° pessoa: '))
    idade = date.today().year - nasc
   
    if idade < 18: 
        tot_n = tot_n + 1
    else:
        tot_s = tot_s + 1
print(f'Ao todo temos {tot_s} pessoas que {verde}já completaram 18 anos{limpa}.')
print(f'E temos {tot_n} pessoas que ainda {vermelho}não atigiram 18 anos{limpa}.')
