# Aula 09 - Manipulando Cadeias de Texto
# Fatiamento - pegar pedaços da string (cadeia de texto)

# [C] [u] [r] [s] [o] [ ] [e] [m] [ ]  [V]  [í]  [d]  [e]  [o]  [P]  [y]  [t]  [h]  [o]  [n]
# [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20] [21]

# Para o python as letras maiúsculas são diferentes das minúsculas.

frase = 'Curso em Vídeo Python'
print(frase[9]) # a contagem inicia em 0, então pega a décima letra que é 'V'.

print(frase[9:14]) # aqui ele pega de 9 aé 14, que imprime a palavra 'Vídeo'. A necessidade de ir até 13  é que nunca pega o último valor, sempre adicionar um no final.

print(frase[9:21]) # 

print(frase[9:21:2]) # Imprimi a string fatiando e saltando de dois em dois 'VdoPto.

print(frase[:5]) # depois dos dois pontos é onde vai terminar, já que não tem um inicio.

print(frase[15:]) # indicou o inicio mas não o final, então ele fatia do 15 em diante.

print(frase[9::3]) # começa no 9 e vai até o final, e o 3 é saltando de três em três