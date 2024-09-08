# Aqui, você está concatenando três strings: 'André', ' ', e 'Camargo'. O resultado é 'André Camargo', que é então impresso.
concatenacao = 'André' + ' ' + 'Camargo'
print(concatenacao)

# error
# O código acima está comentado porque tentaria adicionar uma string ('André') com um número (1). 
# Isso causaria um erro de tipo, já que não é possível somar diretamente uma string com um inteiro.
#concatenacao_error = 'André'+ 1 + ' ' + 'Camargo'
#print(concatenacao_error)

# correção utilizando a coerção
# Aqui, você está corrigindo o erro anterior ao converter o número 1 para uma string com a função str(). 
# Assim, a expressão 'André ' + str(1) + ' ' + 'Camargo' se torna 'André 1 Camargo'.
concatenacao_error = 'André '+ str(1) + ' ' + 'Camargo'
print(concatenacao_error)


# Multiplicando a string 'A' por 10, você obtém 'AAAAAAAAAA', que é impresso.
repeticao = 'A' * 10
print(repeticao)

# Aqui, 'André ' é repetido 6 vezes, resultando em 'André André André André André André ', que é então impresso.
repeticao2 = 6 * 'André '
print(repeticao2)
