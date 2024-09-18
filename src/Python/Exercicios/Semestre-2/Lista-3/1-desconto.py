def calcDiscount(price, discount):
    desc = price * (discount / 100)
    return price - desc


priceProduct = float(input('Informe o valor do produto: '))

if priceProduct > 0:
    member = str(input('Você é membro fidelidade da loja: (sim/não) '))
    print('-'*50)

    if member == 'sim':
        priceProduct =  calcDiscount(priceProduct, 15)
        print(f'Você ganhou 15% de desconto, seu produto irá sair por: {priceProduct:.2f}')
        print('-'*50)
    else:
        priceProduct = calcDiscount(priceProduct, 5)
        print(f'Você ganhou 5% de desconto, seu produto irá sair por: {priceProduct:.2f}')
        print('-'*50)

    compom = str(input('Você tem um cupom de desconto? (sim/não) '))
    print('-'*50)

    if compom == 'sim':

        codigo = str(input('Digite o código do compom: ')).upper()
        print('-'*50)

        match(codigo):
            case 'CUPOM10':
                priceProduct = calcDiscount(priceProduct, 10)
            case 'CUPOM20':
                priceProduct = calcDiscount(priceProduct, 20)

    print(f"O valor do produto é {priceProduct:.2f}")