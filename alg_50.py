import math as m

base = int(input('\ndigite base:'))
altura = int(input('\ndigite altura'))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)

print(f'\nperimetro={perimetro}')
print(f'\narea={area}')
print(f'\ndiagonal={diagonal}')
print('\n')



