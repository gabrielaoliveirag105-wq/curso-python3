# Aula 09 - Análise de String
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ]  [V]  [í]  [d]  [e]  [o]  [P]  [y]  [t]  [h]  [o]  [n]
# [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20] [21]

# Analisando a string, tamanho dela, quantidade de letras, com qual letra começa...

frase = 'Curso em Vídeo Python'
print(len(frase)) # verifica o tamanho da frase - 21 caracteres

print(frase.count('o')) # permite contar quantas letras (a letra escolhida) existem dentro da frase.

print(frase.count('o',0,14)) # ele conta do 0 ao 14, se nesse espaço possui letras 'o'.

print(frase.find('deo')) # encontar/ ele procura quantas vezes achou 'deo' ele diz onde começou que é na posição 11.

print(frase.find('Android')) # dentro do 'find' strings que não existem, retornam -1.

print('Curso' in frase) # ele retorna True ou False, se existir a frase.