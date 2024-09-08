"""
    Funções: Uma função nada mais é do que um conjunto ou bloco de comandos que executam alguma ação ou tarefa.
    Geralmente uma função recebe algum parâmetro, executa uma ação e devolve algum resultado que pode ser chamdo de retorno.
    
    Imagine uma função como um liquidificador, onde você coloca as laranjas nele, bate as laranjas e então você tem um suco de laranja pronto.
"""

def somar(a, b):
    sum = a+b
    return sum

def enviarEmail(email):
    saida = email
    remetente = 'contato@andre.com.br'
    senha = '123'
    
    # Função sem retorno
    
    # Conecta no provedor
    # Monta o corpo do email
    # Envia email


print(somar(1,88))

enviarEmail('andre.camargo@msn.com')

qtd_de_dolares = 1000050.4
print(qtd_de_dolares)

# Aqui, você está formatando o número para incluir separadores de milhar e limitar a duas casas decimais. A expressão :,.2f é um especificador de formato que:
print(f'$ {qtd_de_dolares:,.2f}')


def formatar_reais(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

qtd_de_reais = 1000050.4
formatted_reais = formatar_reais(qtd_de_reais)

print(formatted_reais)

# 1. Formato dos Dólares (USD)
# Separador de Milhar: Vírgula (,)
# Separador Decimal: Ponto (.)

# 2. Formato dos Reais (BRL)
# Separador de Milhar: Ponto (.)
# Separador Decimal: Vírgula (,)