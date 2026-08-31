print('------- DESAFIO 29 ---------')
# Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. Amulta vai custar R$7,00 por cada Km acima do permitido.

from time import sleep
sleep(1.0)

print('---- RADAR DE VELOCIDADE ----')
velo = float(input('Velocidade do carro (km/h): '))
multa = (velo - 80) * 7

if (velo > 80):
    print(f'ATENÇÃO! Você ultrapassou a velocidade permitida de 80km/h. \nSua velocidade foi {velo}km/h, o valor da multa a ser paga é de R${multa:.2f}')
else:
    print(f'PARABÉNS! Sua velocidae foi {velo}km/h, permitida \npara a rodovia que exige a velocidade de 80km/h.')
print('-'*54)
print('Siga com segurança!')