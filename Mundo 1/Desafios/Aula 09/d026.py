print('---------- DESAFIO 26 ----------')
# Faça um programa que leia uma frase pelo teclado e mostre:
""" 
- Quantas vezes aparece a letra 'a'.
- Em que posição aparece a primeira vez
- Em que posição aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra "A": {frase.upper().count('A')}')
print(f'A letra "A" aparece pela primeira vez na posição: {frase.lower().find('a')+1}')
print(f'A última letra "A" aparece na posição: {frase.lower().rfind('a')+1}')