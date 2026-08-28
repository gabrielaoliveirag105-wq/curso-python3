# Aula 10 - Cálculo de Média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi {media:.1f}')

if (media <= 6):
    print(f'Sua média foi {media:.1f}, você consegue melhorar um pouquinho.')
else:
    print(f'Oba! Sua média foi {media:.1f}, continue assim!')
