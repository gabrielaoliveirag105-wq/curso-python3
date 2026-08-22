# Aula 09 - Dividindo String

# [C] [u] [r] [s] [o] [ ] [e] [m] [ ]  [V]  [í]  [d]  [e]  [o]  [P]  [y]  [t]  [h]  [o]  [n]
# [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20] [21]

frase = 'Curso em Vídeo Python'
print(frase.split()) # divide a frase através dos espaços, onde tiver o espaço ele divide (refazendo o índice, colocando em uma nova lista)

print('-'.join(frase)) # junta todos os elememtos de frase separando letra por letra e espaços por esse '-' símbolo.

#DICA: Para escrever em várias linhas sem repetir diversos print() é  só colocar três aspas abrindo e fechando. 

print("""Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde 1966, quando os designers da Letraset e James Mosley, o bibliotecário da St Bride Printing Library em Londres, pegaram uma tradução de Cícero de 1914 e a embaralharam para criar um texto fictício para as folhas de tipos da Letraset. Ele sobreviveu não apenas a muitas décadas, mas também à transição para a editoração eletrônica, permanecendo essencialmente inalterado. Foi popularizado graças a essas folhas e, mais recentemente, com softwares de editoração eletrônica como o Aldus PageMaker e o Microsoft Word, que incluíam versões de Lorem Ipsum.""")

print(frase.upper().count('o')) # permite combinar/unir