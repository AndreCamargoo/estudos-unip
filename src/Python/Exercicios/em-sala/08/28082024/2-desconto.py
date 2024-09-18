"""
    # Lista de Exercícios III

    ### **Exercício 1: Calculadora de Descontos**

    Crie um programa que funcione como uma calculadora de descontos para uma loja. O programa deve:

    - Solicitar o preço original do produto ao usuário.
    - Perguntar se o usuário é membro do clube de fidelidade da loja. Se for, o desconto é de 15%. Se não for,
    o desconto é de 5%.
    - Perguntar se o usuário deseja aplicar um desconto adicional baseado em cupons. Os cupons disponíveis são:
    "CUPOM10" (10% de desconto) e "CUPOM20" (20% de desconto). Caso o cupom inserido seja inválido, o desconto adicional não deve ser aplicado.
    - Calcular e exibir o preço final do produto após aplicar todos os descontos possíveis.

    **Dicas:**

    - Crie uma função para calcular o desconto baseado no clube de fidelidade.
    - Use outra função para aplicar o desconto adicional baseado no cupom fornecido.
    - Lembre-se de utilizar `input()` para capturar os dados dos usuários e `float()` para converter o preço para um número decimal.
"""

priceProduct = float(input('Informe o valor do produto: '))

def calcDiscount(price, discount):
    desc = price * (discount / 100)
    return price - desc

if priceProduct > 0:
    member = str(input('Você é membro fidelidade da loja: (sim/não) '))

    if member == 'sim':
        priceProduct =  calcDiscount(priceProduct, 15)
        print(f'Você ganhou 15% de desconto, seu produto irá sair por: {priceProduct}')
    else:
        priceProduct = calcDiscount(priceProduct, 5)
        print(f'Você ganhou 5% de desconto, seu produto irá sair por: {priceProduct}')

    compom = str(input('Você tem um cupom de desconto? (sim/não) '))

    if compom == 'sim':

        codigo = str(input('Digite o código do compom: ')).upper()

        match(codigo):
            case 'CUPOM10':
                priceProduct = calcDiscount(priceProduct, 10)
            case 'CUPOM20':
                priceProduct = calcDiscount(priceProduct, 20)

    print(f"O valor do produto é {priceProduct:.2f}")
