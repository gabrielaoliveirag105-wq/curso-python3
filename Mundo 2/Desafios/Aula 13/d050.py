print('----- DESAFIO 50 ------')
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('--- CÁLCULO DOS VALORES PARES ---')

soma = 0
cont = 0
for c in range(1,6+1):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Foram digitados {cont} números pares \nA soma dos valores pares vale: {soma}')






































 