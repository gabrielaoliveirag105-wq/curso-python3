# Aula 12 - Testando condicional elif

nome = str(input('Digite seu nome: '))
if nome == 'Gabriela':
    print('Uau, que nome lindo!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Ana':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Lara Sara Sophia Hadassa':
    print('Seu nome é belíssimo, bem diferente.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')