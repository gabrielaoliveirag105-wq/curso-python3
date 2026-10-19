# Aula 17 - Lista com For

valores = list()
for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)

for c,v in enumerate(valores): # mostra a posição onde se encontra cada elemento
    print(f'O valor {v} está na posição {c}')
