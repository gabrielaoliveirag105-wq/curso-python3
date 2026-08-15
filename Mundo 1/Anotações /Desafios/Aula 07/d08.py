print('------ DESAFIO 08 ------') 
# Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros. 

metro = float(input('Digite uma distância (metro): '))
c = metro * 100
m = metro * 1000

print(f'Convertendo {metro} metros em Centímetros obtemos: {c:.0f}cm \nJá convertendo para Milímetros obtemos: {m:.0f}mm ')