print('------ DESAFIO 38 ------')
# Pegue alguns desafios e coloque um sistema de cores.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra \033[4;31m"A"\033[m: \033[1;34m{frase.upper().count('A')}\033[m')
print(f'A letra \033[4;31m"A"\033[m aparece pela primeira vez na posição: \033[1;34m{frase.lower().find('a')+1}\033[m')
print(f'A última letra \033[4;31m"A"\033[m aparece na posição: \033[1;34m{frase.lower().rfind('a')+1}\033[m')