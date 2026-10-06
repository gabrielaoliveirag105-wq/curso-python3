print(' ----- DESAFIO 77 ----- ')
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print('----- LISTAGEM DE VOGAIS -----')
palavras = ('aprender', 'programar', 'persistencia', 'dedicacao', 'motivacao', 'academia', 'correr', 'comer', 'trabalhar', 'carteira', 'confianca')

for palavra in palavras:
    print(f'\nNa palavra \033[1;33m"{palavra}"\033[m temos as vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        