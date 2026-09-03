print('----- DESAFIO 7 ------')
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('----- CONVERSOR DE BASES ------')

num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha a base de conversão:' \
'\n[1] BINÁRIO' \
'\n[2] OCTAL' \
'\n[3] HEXADECIMAL' 
'\nDigite sua opção: '))

print('-'*30)
if opcao == 1:
    print(f'O número {num} em BINÁRIO é {bin(num)[2:]}') # com o fatiamneto mantém somente os dígitos númericos, sem os prefixos.
elif opcao == 2:
    print(f'O número {num} em OCTAL é {oct(num)[2:]}') 
elif opcao == 3:
    print(f'O número {num} em HEXADECIMAL é {hex(num)[2:]}')
else:
    print('\033[1;31mATENÇÃO! Opção Inválida, tente novamente.\033[m')