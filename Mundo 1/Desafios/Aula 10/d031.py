print('------- DESAFIO 31 ---------')
# Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até 200km e R$0,45 para viagens mais longas.

from time import sleep
sleep(1.0)

print('------- PASSAGEM PARA VIAGEM --------')
print('-------------------------------------')
print('|          TABELA DE PREÇO          |')
print('|      <= 200Km - 0,50 (por Km)     |')            
print('|      + de 200Km - 0,45 (por km)   |')               
print('-------------------------------------')

distancia = float(input('Qual a distância da sua viagem (Km): '))

if (distancia <= 200):
    passagem = distancia * 0.50
    print(f'O percurso da sua viagem tem {distancia}Km.\nO valor da passagem ficou R${passagem:.2f}.')
else:
    passagem = distancia * 0.45
    print(f'O percurso da sua viagem tem {distancia}Km.\nO valor da passagem será R${passagem:.2f}.')
