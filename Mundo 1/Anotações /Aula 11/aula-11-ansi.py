# Aula 11 - Trabalhando com cores no terminal

# - ANSI - escape sequence (funciona em uma enorme variedade de ambientes)

# Código ANSI:
# O códico começa com um contra barra e logo depois vem o código
print('\033[0;33;44m') # 0 - estilo, 33 - texto, 44 - backgorund 

# Lista de estilo de texto:
""" 
0 - None (nenhum estilo)
1 - Negrito
4 - Sublinhado
7 - Negative (inverte as configurações)
"""

# Lista de cores de texto:
"""
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Roxo
36 - Azul piscina (ciano)
37 - Cinza
"""

# Lista de cores de fundo (background):
"""
40 - Branco
41 - Vremelho
42 - Verde 
43 - Amarelo
44 - Azul
45 - Lilás/Roxo
46 - Azul piscina (ciano)
47  - Cinza
"""

# Teste: 
print('\033[0;30;41mFundo Veremlho')
print('\033[4;33;44mFundo Azul')
print('\033[1;35;43mFundo Amarelo')
print('\033[30;42mFundo Verde')
print('\033[mFundo Preto')
print('\033[7;40mFundo Branco')