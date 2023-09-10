import math as m

sm = float(input('\nentre com o salario minimo:'))
qtdade = float(input('\nentre com a quantidade em quilowatt:'))
preco = sm/700
vp = preco*qtdade
vd = vp*0.9

print(f'\npreco do quilowatt:{preco} \nvalor a ser pago:{vp} \nvalor com desconto:{vd}')
print('\n')

