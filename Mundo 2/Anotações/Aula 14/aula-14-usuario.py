# Aula 14 - Estrutura com interação do usuário
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Você deseja continuar? [S/N] ')).upper() #aqui deixa o usuário escolher se quer continuar
print('Fim')
