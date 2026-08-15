print('----- DESAFIO 12 ------')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

produto = input('Qual o produto que você comprou? ')
preco = float(input('E qual o valor desse produto? R$ '))
desconto = preco - (preco * 5/100) 

print(f'Que maravilha. O produto está com um super desconto. \nCom o desconto de 5%, esse produto custou R${desconto:.2f}.')
