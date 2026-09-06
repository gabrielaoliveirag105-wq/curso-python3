# Aula 13 - Inserindo dados na Repetição

soma = 0 # soma recebe 0 pois nehum valor foi somado ainda 
for c in range (0,3):
    n = int(input('Digite um valor: '))
    soma = soma + n # a soma é realizada dentro do laço 
print(f'A soma vale: {soma}') # e deve ser mostrada fora do laço
print('Fim')