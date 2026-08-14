# Aula 07 - Ordem de precedência dos operadores:
# (operadores que vão ser executados primeiro)

# 1. () - Parênteses
# 2. ** - Potência
# 3. * / // % - Multiplicação, Divisão, Divisão inteira e Resto da divisão
# 4. + - - Adição e Subtração

print(5 + 3 * 2)  # Resolvemos a multiplicação primeiro, depois a adição.

print(3 * 5 + 4 ** 2) # Resolvemos primeiro a potência, depois a multiplicação e por último a adição.

print(3 * (5 + 4) ** 2) # Resolvemos primeiro o que está dentro dos parênteses, depois a potência e por último a multiplicação.