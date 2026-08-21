# Aula 08 - Utilizando Módulos

# Exemplo:
# import bebida - vai importar todas as bebidas.
# from doce import pudim - adicionando o from, conseguimos especificar o doce que queremos, não vem tudo.

# math - matemática
# ceil - arredondamento para cima / floor - arredondamento para baixo
# trunch - elimina da vírgula em diante / pow - potência
# sqrt - RaizQuad. / factorial - cálculo de fatorial
# para importar duas bibliotecas é só utilizar a vírgula 
# - from match import sqrt, floor


import math
n1 = int(input('Digite um núemro: '))
raiz = math.sqrt(n1) # importção 
print(f'A raiz de {n1} é {raiz:.2f}.')
print(f'A raiz de {n1} é {math.ceil(raiz)}') # para arredondar para cima.
print(f'A raiz de {n1} é {math.floor(raiz)}') # para arredondar para baixo.


 
