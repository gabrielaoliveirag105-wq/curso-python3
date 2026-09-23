print('----- DESAFIO 61 ------')
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=== 10 TERMOS DE UMA PA ===')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

c = 1
while c <= 10:
    print(termo, end=' -> ')
    termo = termo + razao
    c = c + 1
print('ACABOU!')
