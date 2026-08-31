print('------ DESAFIO 37 ------')
# Pegue alguns desafios e coloque um sistema de cores.

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é \033[4;34m{type(n)}\033[m.')
print(f'Contém apenas letras? \033[1;31m{n.isalpha()}\033[m')
print(f'Contém apenas números? \033[4;33m{n.isnumeric()}\033[m')
print(f'Contém letras e números? \033[36m{n.isalnum()}\033[m')
print(f'Todas as letras são maiúsculas? \033[1;34m{n.isupper()}\033[m')
print(f'Todos os caracteres podem ser exibidos? \033[4;37m{n.isprintable()}\033[m')
print(f'Contém apenas espaços? \033[1;32m{n.isspace()}\033[m')
print(f'Todas as letras são minúsculas? \033[m{n.islower()}\033[m')
print(f'Contém apenas dígitos? \033[1;35m{n.isdigit()}\033[m')
print(f'Contém apenas caracteres decimais? \033[7;40m{n.isdecimal()}\033[m')
print(f'Está captalizado? \033[4;35m{n.istitle()}\033[m')