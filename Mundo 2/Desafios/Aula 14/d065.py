print('----- DESAFIO 65 ------')
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

amarelo = '\033[1;33m'
limpa = '\033[m'

print(' === AVALIANDO VALORES === ')
c = soma = maior = menor = 0
resp = 'S'

while resp == 'S':
    n = int(input('Digite um número: '))
    c = c + 1
    soma = soma + n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('\033[1;31mVocê deseja continuar? [S/N] \033[m')).upper()

media = soma / c
print(f'A soma de todos os {amarelo}{c}{limpa} valores vale {amarelo}{soma}{limpa} e sua média é {amarelo}{media:.1f}{limpa}')
print(f'O {amarelo}maior{limpa} valor digitado foi {amarelo}{maior}{limpa} e o {amarelo}menor{limpa} foi {amarelo}{menor}{limpa}')
