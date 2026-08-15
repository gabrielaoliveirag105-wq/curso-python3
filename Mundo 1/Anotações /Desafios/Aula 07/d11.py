print('------- DESAFIO 11 ----------')
# Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

a = float(input('Qual a altura da parede (metros): '))
l = float(input('E qual a largura dela (metros): '))
area = l * a
tinta = area / 2 

print(f'\nA largura é {l}m e a altura é {a}m \nSua área total vale {area}m \nPara pintar a área toda será preciso de {tinta} litros de tinta.')
