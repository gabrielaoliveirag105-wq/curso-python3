print('----- DESAFIO 41 ------')
"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date
from time import sleep
print('----- CATEGORIA DE NATAÇÃO ------')
nome = str(input('Nome do (a) atleta: '))
ano_nasc = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('-'*33)

sleep(1)
if idade <= 9:
    print(f'Atleta possui {idade} anos \nCategoria: MIRIM.')
elif idade <= 14:
    print(f'Atleta possui {idade} anos \nCategoria: INFANTIL.')
elif idade <= 19:
    print(f'Atleta possui {idade} anos \nCategoria: JÚNIOR.')
elif idade <= 25:
    print(f'Atleta possui {idade} anos \nCategoria: SÊNIOR.')
else:
    print(f'Atleta possui {idade} anos \nCategoria: MASTER.')
