conta = int(input('\nDigite conta de três dígitos:'))
d1 = conta//100
d2 = conta%100//10
d3 = conta%100%10
inv = d3*100+d2*10+d1
soma = conta+inv
d1 = (soma//100)*1
d2 = (soma%100//10)*2
d3 = (soma%100%10)*3
dígito = (d1+d2+d3)%10

print(f'\ndígito verificador: {dígito}')
print('\n')

