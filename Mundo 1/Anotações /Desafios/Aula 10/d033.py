print('------- DESAFIO 33 ---------')
# Faça um programa que leia três números e mostre qual é o maior e qual o menor:

n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))
n3 = int(input('E por fim, escolha o terceiro número: '))

# Verificando o maior 
if (n1 >= n2 and n1 >= n3):
    print(f'O maior número é {n1}')
else:
    if (n2 >= n1 and n2 >= n3):
        print(f'O maior número é {n2}')
    else:
        print(f'O maior número é {n3}')

# Verificando o menor 
if (n1 <= n2 and n1 <= n3):
    print(f'O menor número é {n1}')
else:
    if (n2 <= n1 and n2 <= n3):
        print(f'O menor número é {n2}')
    else:
        print(f'O menor número é {n3}')
    
