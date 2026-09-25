print('----- DESAFIO 68 ------')
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

vermelho = '\033[1;31m' 
limpa = '\033[m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
import random 

print(f'{amarelo} === ÍMPAR OU PAR === {limpa}')
print('-'*40)
print('  Está pronto para jogar? Vamos lá! ')
print('-'*40)

vitoria = 0

while True:
    parouimpar = ' '
    valor = random.randint(0,10)
    computador = 'I'
 
    num = int(input('Escolha um número: '))
    soma = num + valor
    
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print(f'Você jogou {num} e o computador {valor} e o total é: {soma}')
        
    if soma % 2 == 0:
        if parouimpar == 'P':
            print(f'{verde}Deu par, você VENCEU!{limpa}')
            vitoria = vitoria + 1
        else:
            print(f'{vermelho}Deu par, você PERDEU!{limpa}')
            break
        print('-'*35)
    else:
        if parouimpar == 'I':
            print(f'{verde}Deu ímpar, você VENCEU!{limpa}')
            vitoria = vitoria + 1
        else:
            print(f'{vermelho}Deu ímpar, você PERDEU!{limpa}')
            break
        print('-'*35)
  
print(f'{amarelo}Ao todo você venceu {vitoria} rodadas!{limpa}')
