print('------ DESAFIO 37 ------')
# Pegue alguns desafios e coloque um sistema de cores.

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

nome = input('Nome do funcionário: ')
sal = float(input('Salário atual: '))
novo = sal + (sal * 15/100)

print(f'Com um aumento de 15%, o novo salário do (a) funcionário (a) \033[4;33m{nome}\033[m será R$ \033[1;32m{novo:.2f}\033[m')

