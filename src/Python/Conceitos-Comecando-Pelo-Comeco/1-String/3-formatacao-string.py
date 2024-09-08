nome = 'André'
sobrenome = 'Camargo'


print('Meu nome é: ',nome, sobrenome)

# Neste trecho, você está concatenando nome e sobrenome com um espaço entre eles. A variável nome_completo terá o valor 'André Camargo', e a saída será:
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

# Aqui, você está utilizando uma f-string para formatar a string de maneira mais legível e concisa. A saída será:
print(f'Meu nome é {nome} {sobrenome}')
