# Aula 13 - Utilizando Condições dentro da Repetição
# É possível colocar uma estrutura condicional dentro do laço de repetição.

# ele não considera o último valor, portanto o ideal é sempre acrescentar um á mais. 10+1 = 11, assim ele mostra o valor 10. 

for c in range (1,11): 
    print(c)
    if c == 10:
        print('\nEstamos finalizando a contagem...') # veja a identação, e o que está dentro do outro é um aninhamento.
print('Saindo do programa')