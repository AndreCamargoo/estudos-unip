numero = input('Digite seu número: ')

# if não evita erros

# if numero.isdigit():
#     numero_float = float(numero)
#     print(f'O dobro de {numero_float} é {numero_float*2:.2f}')
# else:
#     print('Isso não é um número')

# Try trata os erros mandando para except (somente exemplo try não é usado dessa forma)
try:
    numero_float = float(numero)
    print(f'O dobro de {numero_float} é {numero_float*2:.2f}')
except:
    print('Isso não é um número')



