print('----- DESAFIO 69 ------')
'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

print('=== VALIDAÇÃO DE DADOS === ')

pessoas = homem = mulher = 0


while True:
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe sua idade: '))
    sexo = ' ' 
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: ')).upper().strip()[0]

    if idade >= 18:
        pessoas = pessoas + 1

    if sexo in 'Mm':
        homem = homem + 1

    if sexo in 'Ff' and idade < 20:
        mulher = mulher + 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    print('-' * 35)

    if resp == 'N':
        break

print(f'Ao todo temos {pessoas} pessoas com mais de 18 anos.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'Ao todo  temos {mulher} mulheres com menos de 20 anos.')
