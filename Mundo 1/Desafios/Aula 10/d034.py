print('------- DESAFIO 34 ---------')
# Escreva um programa que prgunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

fun = str(input('Nome do funcionário: '))
sal = float(input('Informe o salário atual: R$'))

if (sal > 1250):
    aumento = sal * (10/100) 
    novo_sal = sal + aumento
    print(f'Com um aumento de R${aumento:.2f} reais, o (a) \nfuncionário (a) {fun} passa a receber R${novo_sal:.2f}.')
else:
    aumento = sal * (15/100)
    novo_sal = sal + aumento
    print(f'Com um aumento de R${aumento:.2f} reais, o (a) \nfuncionário (a) {fun} passa a receber R${novo_sal:.2f}')