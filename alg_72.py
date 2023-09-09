depósito = float(input('\nentre com depósito'))
taxa = float(input('\nentre com a taxa de juros:'))
valor = depósito*taxa/100
total = depósito + valor

print(f'\nRendimentos: {valor} \nTotal: {total}')
print('\n')
