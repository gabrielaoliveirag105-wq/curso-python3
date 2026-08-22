print('---------- DESAFIO 26 ----------')
# Faça um programa que leia uma frase pelo teclado e mostre:
""" 
- Quantas vezes aparece a letra 'a'.
- Em que posição aparece a primeira vez
- Em que posição aparece a última vez.
"""

frase = str(input('Digite uma frase: '))
letra = frase.upper().count('A')
primeira = frase.lower().find('a')
ultima = frase.lower().rfind('a')

print(f'Quantas vezes aparece a letra "A": {letra}')
print(f'A letra "A" aparece pela primeira vez na posição: {primeira}')
print(f'A última letra "A" aparece na posição: {ultima}')