# Aula 13 - Lendo um valor 

# lê até o valor que foi escolhido pelo usuário.
n = int(input('Digite um valor: '))
for c in range(0, n+1):
    print(c)
print('\nFim...')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Escolha o passo: '))

for c in range (i, f+1, p):
    print(c)
print('Programa finalizado')