# Aula 14 - Fazendo testes com a estrutua While 

# Aqui verifica se o valor é par e quantos numeros pares e ímpares tem.
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Ao todo temos {par} números pares e {impar} números ímpares.')
