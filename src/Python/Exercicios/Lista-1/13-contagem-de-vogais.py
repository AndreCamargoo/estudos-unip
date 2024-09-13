frase = input('Digite sua frase: ')

vogais = 'aeiou'
contagem = 0

for letra in frase:
    if letra in vogais:
        contagem +=1
        

print(f'Número de vogiais encontradas é: {contagem}')
