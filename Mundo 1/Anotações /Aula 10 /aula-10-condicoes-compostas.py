# Aula 10 - Condicionais Compostas
# A condicional composta já permite o segundo 'caminho'.

nome = str(input('Digite seu nome: '))
if (nome == 'Gabriela'):
    print('Nossa, que nome lindo!')
else:
    print('Seu nome é bem comum.') # Se o primeiro bloco não for verdadeiro, esse é executado.
print(f'Bom dia, {nome}.')