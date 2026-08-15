print('----- DESAFIO 13 -------')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

nome = input('Nome do funcionário: ')
sal = float(input('Salário atual: '))
novo = sal + (sal * 15/100)

print(f'Com um aumento de 15%, o novo salário do (a) funcionário (a) {nome} será R$ {novo:.2f} ')

