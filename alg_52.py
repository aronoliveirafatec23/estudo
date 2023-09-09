import math as m

lado = int(input('\ndigite o lado do quadrado:'))
perimetro = 4*lado
area = lado**2
diagonal = lado*m.sqrt(2)

print(f'\nperimetro:{perimetro}')
print(f'\narea:{area}')
print(f'\ndiagonal:{diagonal}')
print('\n')

