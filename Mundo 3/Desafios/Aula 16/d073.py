print(' ----- DESAFIO 73 ----- ')
'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

print('------ CAMPEONATO BRASILEIRO ------')

times = ('Flamengo', 'Palmeiras', 'Athetico-PR', 'Fluminense', 
         'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba', 'Bragantino', 'São Paulo', 'Botafogo', 'EC Vitória', 'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio', 'Internacional', 'Remo', 'Chapecoense')

print(f'Lista de times do Brasileirão: {times}')
print('-'* 50)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('-'*50)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-'* 50)
print(f'Os times em ordem alfabética ficam: {sorted(times)}')
print('-'* 50)
print(f'O time da Chapecoense esta na posição: {times.index("Chapecoense") + 1}')