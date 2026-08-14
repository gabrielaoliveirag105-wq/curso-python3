# Aula 07 - Persoalizando a saída de dados com máscaras de formatação

nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer, {nome:20}!') # O número 20 indica que o nome será exibido em um campo de 20 caracteres.

print(f'Prazer em te conhecer, {nome:>20}!') # Alinhamento à direita.

print(f'Prazer em te conhecer, {nome:<20}!') # Alinhamento à esquerda.

print(f'Prazer em te conhecer, {nome:^20}!') # Alinhamento no centro.

print(f'Prazer em te conhecer, {nome:-^20}!') # Alinhamento no centro, com o sinal '-' preenchando os espaços vazios

print(f'Prazer em te conhecer, {nome:->20}!') # Alinhamento à direita, com o sinal '-' preenchendo o espaço em branco