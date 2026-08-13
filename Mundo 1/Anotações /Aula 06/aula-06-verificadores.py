# Aula 06 - Verificando tipos primitivos de dados

n = input('Digite um número: ')
print(n.isnumeric()) # Verifica se é númerico (somente números)
print(n.isalpha()) # verifica se é alfabético (somente letras)
print(n.isalnum()) # Verifica se é alfanumérico (letras e números)
print(n.isupper()) # Verifica se todas as letras estão em maiúsculo

# Fora esses métodos, existem outros como: n.islower(), n.isspace(), n.isdecimal(), etc.