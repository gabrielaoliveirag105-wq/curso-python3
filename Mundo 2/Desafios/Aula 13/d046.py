print('----- DESAFIO 46 ------')
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

azul = '\033[1;44m' 
limpa = '\033[m'
amarelo = '\033[4;33m'

print(f'{azul}--- CONTAGEM REGRESSIVA 💥 ---{limpa}')

for c in range (10,-1,-1):
    print(c)
    sleep(1)
print(f'{amarelo}FELIZ ANO-NOVO! SEJA BEM-VINDO 2027{limpa} 🎆')