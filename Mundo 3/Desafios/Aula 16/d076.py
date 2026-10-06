print(' ----- DESAFIO 76 ----- ')
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('----- LISTAGEM DE PREÇOS -----')
print('-'*43)
produtos = ('Esmalte', 5.50, 
            'Base', 65.00, 
            'CB 300f', 15000.00, 
            'Pneu', 250.00, 
            'Tênis', 150.00, 
            'Saia', 65.00, 
            'Cômoda', 350.00, 
            'Mala', 120.00, 
            'Perfume', 180.00, 
            'Batom', 15.00)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:30}', end='')
    else:
        print(f'R${produtos[pos]:.2f}')
print('-'*43)
