print('----- DESAFIO 47 ------')
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('--- SOMENTE NÚMEROS PARES --- ')

from time import sleep
for c in range(1, 50+1):
    if c % 2 == 0:
        print (c)
        sleep(0.5)
print('\033[4;33m\nPrograma finalizado!\033[m')