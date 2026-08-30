print('------ DESAFIO 36 ------')
# Pegue alguns desafios dos 30 que foi passado e adicione cores.

# Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. Amulta vai custar R$7,00 por cada Km acima do permitido.

from time import sleep
sleep(1.0)

print('\033[1;30;43m---- RADAR DE VELOCIDADE ----\033[m')
velo = float(input('Velocidade do carro (km/h): '))
multa = (velo - 80) * 7

if (velo > 80):
    print(f'\033[31mATENÇÃO! Você ultrapassou a velocidade permitida de 80km/h. \nSua velocidade foi {velo}km/h, o valor da multa a ser paga é de R${multa:.2f}\033[m')
else:
    print(f'\033[34mPARABÉNS! Sua velocidae foi {velo}km/h, permitida \npara a rodovia que exige a velocidade de 80km/h.\033[m')
print('-'*54)
print('Siga com segurança!')