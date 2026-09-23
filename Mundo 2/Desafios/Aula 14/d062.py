print('----- DESAFIO 62 ------')
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('===  TERMOS DE UMA PA ===')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

c = 1
mais_termos = 10
total_termos = 0

while mais_termos != 0:
    total_termos = total_termos + mais_termos
    while c <= total_termos:
        print(termo, end=' -> ')
        termo = termo + razao
        c = c + 1
    print('Pausa')
    mais_termos = int(input('\nQuantos termos você quer mostrar a mais? \033[1;31m[0 para finalizar] \033[m'))

print(f'Progressão finalizada! Foram mostrados \033[4;33m{total_termos} termos\033[m.')
