print('----- DESAFIO 55 ------')
#  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

vermelho = '\033[4;31m'
verde = '\033[4;32m'
limpa = '\033[m'

print('=== DETECTOR DE PESO ===')

maior = 0
menor = 0

for c in range (1, 6):
    nome = str(input('Nome: '))
    peso = float(input('Peso (kg): '))
    print('-' * 20)

    # aqui fazemos a checagem do primeiro valor lido que para o programa sempre vai ser o mneor e o maior, até por que foi o único valor lido até o momento
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O {verde}maior{limpa} peso informado foi {verde}{maior}Kg{limpa}')
print(f'O {vermelho}menor{limpa} peso informado foi {vermelho}{menor}Kg{limpa}')