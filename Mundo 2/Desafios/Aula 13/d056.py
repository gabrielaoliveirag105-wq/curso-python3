print('----- DESAFIO 56 ------')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

amarelo = '\033[4;33m'
limpa = '\033[m'

print('=== ANÁLISE DE PESSOAS ===')

media = 0
soma = 0
nome_maior = 0
maior_idade = 0
mulher = 0
 
for c in range(1,5):
    print(f'\n{amarelo}---  {c}° PESSOA  ---{limpa}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip()
    soma = soma + idade
    media = soma / 2

    if c == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_maior = nome
    if sexo in 'mM' and idade > maior_idade:
        maior_idade = idade
        nome_maior = nome

    if sexo in 'fF' and idade < 20:
        menor_idade = idade 
        mulher = mulher + 1

print(f'A média de idade do grupo é de {amarelo}{media:.0f} anos.{limpa}')
print(f'O homem mais velho é {amarelo}{nome_maior}{limpa}, com {amarelo}{maior_idade} anos{limpa}.')
print(f'Ao todo temos {amarelo}{mulher} mulheres{limpa} com {amarelo}menos{limpa} de {amarelo}20 anos{limpa}.')