valorProtudo = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))

calcDesconto = valorProtudo - ( valorProtudo * desconto / 100)

print(f'O valor do produto era {valorProtudo} com o desconto ficou {calcDesconto}')