print('----- DESAFIO 70 ------')
'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print(' === SUPER ATACADO === ')
print('Barato só se for de graça!')
print('-' * 35)


total = caro = menor = 0
c = 0
barato = ''

while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor do produto: R$'))
    print('-' * 35)

    total = total + valor

    if valor > 1000:
        caro = caro + 1

    if c == 0 or valor < menor:
       menor = valor
       barato = produto
    c = c + 1

    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer adicionar mais algum produto [S/N]? ')).upper().strip()[0]

    if resp == 'N':
        break

print(f'O valor final da sua compra é de R${total:.2f} reais.')
print(f'Ao todo temos {caro} produtos que custaram mais de R$1000 reais.')
print(f'O produto mais barato comprado foi {barato} que custou R${menor}')