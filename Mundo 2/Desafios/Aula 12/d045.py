print('----- DESAFIO 45 ------')
# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('---- JOKENPÔ ----')
print('Você está preparado para jogar? Vamos lá!')
print('------------------------------------------')

sleep(1)

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)
jogador = input('Escolha uma opção: \n---> Pedra, Papel ou Tesoura: ').capitalize()

if jogador not in opcoes:
    print('Opção inválida. Tente novamente.')
if jogador == computador:
    print(f'Empate! escolhemos {computador}. Vamos jogar novamente!')
elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador =='Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
    print(f'\033[1;32mVocê venceu!\033[m Eu escolhi {computador} e você {jogador}. \nParabéns, mas vamos jogar novamente!')
else:
    print(f'Você perdeu! Eu escolhi {computador} e você {jogador}. \nVamos jogar novamente!')