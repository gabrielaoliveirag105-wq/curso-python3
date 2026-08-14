# Aula 07 - Personalizando sintaxe:

n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro valor: '))
soma = n1 + n2
mult = n1 * n2
d = n1 / n2
div = n1 // n2
e = n1 ** n2

print(f'A soma vale {soma}, o produto vale {mult} e a divisão vale {d:.2f} ')
print(f'Divisão inteira vale {div} e a potência vale {e}')

# O uso do ':.2f' permite escolher quantas casas decimais será exibidas.

print(f'A soma vale {soma} o produto vale {mult} e a divisão vale {d:.2f}',end='')
print(f' Divisão inteira vale {div} e a potência vale {e}')

# O end='' - com espaço em branco evita a quebra de linha do primeiro print. 

print(f'A soma vale {soma}, o produto vale {mult} e a divisão vale {d:.2f}', end='>>>')
print(f' Divisão inteira vale {div} e a potência vale {e}')

# É possível adicionar algo dentro das aspas.

print(f'A soma vale {soma} \no produto vale {mult}\ne a divisão vale {d:.2f}',end='')
print(f' Divisão inteira vale {div} e a potência vale {e}')

# O '\n' permite quebrar essa linha em qualquer lugar do print.