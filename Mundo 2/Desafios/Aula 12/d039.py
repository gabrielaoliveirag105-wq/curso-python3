print('----- DESAFIO 39 ------')
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from time import sleep
from datetime import date

sleep(1)
print('----- ALISTAMENTO MILITAR ------')

nome = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print(f'O jovem {nome} ainda \033[1;31mnão tem idade\033[m para se alistar, pois possui {idade} anos. \nAinda falta {18 - idade} anos para o alistamento militar.')
elif idade == 18:
    print(f'O jovem {nome} possui {idade} anos, portanto \033[1;31mestá na hora\033[m de se alistar.')
else:
    print(f'ATENÇÂO! O jovem {nome} \033[1;31mjá passou do prazo de alistamneto\033[m, pois possui {idade} anos. \nJá se passaram {idade - 18} anos do prazo de alistamento.')