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