# Aula 10 - Condições/ Parte 1
# Condições permite que você siga 'caminhos'.
# Identação - é um espaço para a direita dentro do seu bloco de comando.
""" exemplo: 
   if carro.esquerda():
        bloco True #primeiro bloco a ser executado, se esse bloco não for verdadeiro, o bloco True é executado
    else:
        bloco False
"""
# As duas condições não podem ser executadas ao mesmo tempo, ou será True ou False, nunca juntas.

# Exemplo carro:
tempo = int(input('Quantos anos tem seu carro? '))
if (tempo <= 5):
    print(f'Seu carro só tem {tempo} anos, está novinho.')
else:
    print(f'Seu carro já tem {tempo} anos, já é tempo de ficar de olho. ')
print('---- Fim do programa ----') # Todo comando colado ao lado esquerdo sempre vai acontecer.