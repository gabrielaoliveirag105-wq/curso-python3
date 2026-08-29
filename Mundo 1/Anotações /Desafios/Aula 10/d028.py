print('------- DESAFIO 28 ---------')

# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuŕio tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
sleep(1.0)

print('-'*60)
print('     VAMOS JOGAR?     ')
print('Estou pensando em um número entre 0 e 5.... Tente adivinhar!')
print('-'*60)

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))

if (jogador == computador):
    print(f'Parabéns, eu pensei exatamente no número {computador} e você ganhou. \nVamos de novo que agora eu vou ganhar!')
else:
    print(f'Eu sou ótimo nesse jogo, pensei no número {computador}.')
print('Jogue mais uma vez! ')
