print('----- DESAFIO 49 ------')
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

amarelo = '\033[1;33m'
limpa = '\033[m'
verde = '\033[4;32m'

from time import sleep

print(f'{amarelo}--- TABUADA ---{limpa}')
num = int(input('Escolha um número para ver a tabuada: '))

sleep(1)
print(f'{amarelo}\nGerando tabuada...{limpa}')
sleep(1)
    
for c in range (0, 10+1):
    resul = c * num
    print(f'{num} X {c} = {resul}')
print(f'{verde}Continue seus estudos, até a próxima!{limpa}')
