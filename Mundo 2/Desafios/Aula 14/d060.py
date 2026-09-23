print('----- DESAFIO 60 ------')
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

print(' === CÁLCULO DE FATORIAL === ')
n = int(input('Escolha um valor: '))

resultado = 1 # Acumula o resultado do loop 

for n in range (n,0,-1):
    print(n, end=' x ')
    resultado = resultado * n
print(f'= {resultado}')