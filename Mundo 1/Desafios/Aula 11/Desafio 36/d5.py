print('------ DESAFIO 36 ------')
# Pegue alguns desafios dos 30 que foi passado e adicione cores.

# Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até 200km e R$0,45 para viagens mais longas.

from time import sleep
sleep(1.0)

print('------- PASSAGEM PARA VIAGEM --------')
print('\033[7;40m-------------------------------------')
print('|          TABELA DE PREÇO          |')
print('|      <= 200Km - 0,50 (por Km)     |')            
print('|      + de 200Km - 0,45 (por km)   |')               
print('-------------------------------------\033[m')

distancia = float(input('Qual a distância da sua viagem (Km): '))

if (distancia <= 200):
    passagem = distancia * 0.50
    print(f'O percurso da sua viagem tem {distancia}Km.\nO valor da passagem ficou \033[4;33mR${passagem:.2f}\033[m.')
else:
    passagem = distancia * 0.45
    print(f'O percurso da sua viagem tem {distancia}Km.\nO valor da passagem será \033[4;33mR${passagem:.2f}\033[m.')
