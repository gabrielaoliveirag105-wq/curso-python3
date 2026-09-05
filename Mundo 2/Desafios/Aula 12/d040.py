print('----- DESAFIO 40 ------')
"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO""" 

print('----- MÉDIA ESCOLAR ------')
nome = str(input('Nome do (a) aluno (a): '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'O (a) aluno (a) {nome} obteve média {media:.1f} \n\033[4;31mALUNO REPROVADO\033[m.')
elif media >= 5.0 and media <= 6.9:
    print(f'O (a) aluno (a) {nome} obeteve média {media:.1f} \n\033[4;33mALUNO EM RECUPERAÇÃO\033[m.') 
else:
    print(f'O (a) aluno (a) {nome} obteve média {media:.1f} \n\033[4;32mALUNO APROVADO\033[m.')