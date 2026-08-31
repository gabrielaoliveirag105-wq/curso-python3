# Aula 12 - Condições Aninhadas

# Como o próprio nome sugere, é uma estrutura dentro da outra, como um ninho mesmo.
# elif = else/if o famoso 'se senao'.
# Sempre terá um if, nunca começa com elif, e não precisa necessariamente de um else.
# Dentro de um if, você consegue usar quantos 'elif' quiser.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media <= 4.0:
    print(f'Sua nota foi {media:.1f} \nAluno REPROVADO!')
elif media <= 6.0:
    print(f'Sua nota foi {media:.1f} \nAluno em RECUPERAÇÃO!')
else:
    print(f'Sua nota foi {media:.1f} \nAluno APROVADO!')
print('Continue sempre estudando!')