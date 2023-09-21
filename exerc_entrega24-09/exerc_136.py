nome = str(input('\nEntre com nome:'))
idade = int(input('\nEntrec com a idade:'))

if (idade <= 10 ):
    print(f'\n {nome} pagará R$ 30.00 reais.')

elif (idade <= 29):
    print(f'\n {nome} pagará R$ 60.00 reais.')

elif (idade <= 45):
    print(f'\n {nome} pagará R$ 120.00 reais.')

elif (idade <= 59):
    print(f'\n {nome} pagará R$ 150.00 reais.')

elif (idade <= 65):
    print(f'\n {nome} pagará R$ 250.00 reais.')

else:
    print(f'\n {nome} pagará R$ 400.00 reais.')


print('\n')
    
    


    