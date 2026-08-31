print('---------- DESAFIO 22 ----------')
"""" Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com tdas nimúsculas.
- Quantas letras ao todo sem considerar espaços
- Quantas letras tem o primeiro nome """

nome = str(input('Como é o seu nome completo? ')).strip()

print(f'Seu nome em letras maiúsculas fica: {nome.upper()}')
print(f'Veja ele em letras minúsculas: {nome.lower()}')
print(f'Sem considerar os espaços seu nome tem {len(nome) - nome.count(' ')} letras.')
print(f'O primeiro nome possui {nome.find(' ')} letras.')