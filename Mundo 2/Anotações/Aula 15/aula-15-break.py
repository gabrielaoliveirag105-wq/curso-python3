# Aula 15 - Utilizando o Comando break
# O break quebra o loop que está acontecendo em uma sequência de vezes, assim finalizando a repetição e saindo do programa.

n = s = 0
while True:
    n = int(input('Escolha um número: '))
    if n == 999:
        break # ponto de parada e saída do programa
    s = s + n # a soma ocorre após a verificação
print(f'A soma vale {s}') # desconsidera o valor de parada e faz a soma dos valores lidos.