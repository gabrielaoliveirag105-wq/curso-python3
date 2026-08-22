# Aula 09 -Transformando Strings

# [C] [u] [r] [s] [o] [ ] [e] [m] [ ]  [V]  [í]  [d]  [e]  [o]  [P]  [y]  [t]  [h]  [o]  [n]
# [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20] [21]

frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android')) # ele permite a substituição do elemento escolhido, Python por Android (substitui de uma forma 'secundária')

print(frase.upper()) # Todas as letras em maiúsculas (o que é masiusculo se mantem.)

print(frase.lower()) # Todas as letras em minúsculas ( o que é minúsculo se mantem.)

print(frase.capitalize()) # somente o primeiro caractere fica maiúsxulo, o resto é jogado para minúsculo.

print(frase.title()) # ele analisa através dos espaços a quebra de palavras, e transforma o que é minúsculo em maiúscula.

print(frase.strip()) # ele remove todos os espaços (do inicio ao fim) que não possuem necessidade.

print(frase.rstrip()) # ele remove todos os espaços (da direita) que não possuem necessidade.

print(frase.lstrip()) # ele remove todos os espaços (da esquerda) que não possuem necessidade.

