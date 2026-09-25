print('----- DESAFIO 67 ------')
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

c = 1
n = 0
while True:
    print('\033[4;33m===  TABUADA  ===\033[m')
    n = int(input('Escolha um número para ver a tabuada: '))
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n * c}')
        c = c + 1
    print('-'*40)
print('\033[4;31mPrograma finalizado! Até a próxima!\033[m')

    

    
    
    
    