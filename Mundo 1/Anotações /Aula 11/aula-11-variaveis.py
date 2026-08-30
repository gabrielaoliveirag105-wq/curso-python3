# Aula 11 - Colocando cores em variáveis

a = 3
b = 5
print(f'A soma dos valores \033[33m{a}\033[m e \033[34m{b}\033[m vale \033[31m{a+b}\033[m.')

# Outra forma de adicionar cores: 
nome = 'Gabriela'
print(f'Muito prazer te conhecer, \033[4;36m{nome}\033[m!')

# Listando cores: 
nome = 'Gabriela'
cores = {'limpa': '\033[m', 
         'azul': '\033[34m', 
         'amarelo': '\033[33m', 
         'pretoebranco': '\033[7;40m'}
print(f'Olá, {cores["amarelo"]}{nome}{cores["limpa"]}! Seja muito bem-vindo(a).') # você consegue adicionar qualquer cor através da lista acima.

