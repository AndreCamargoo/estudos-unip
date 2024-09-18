"""
    ### Desafio 1

    **
    Embaralha palavra**. Construa uma função que receba uma string como parâmetro e devolva outra string com os
    carateres embaralhados. Por exemplo: se função receber a palavra *python*, pode
    retornar *npthyo*, *ophtyn* ou qualquer outra combinação possível, de forma aleatória.
    Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
    independentemente de como foram digitados.
"""

# Resultado determinístico    
def embaralhar_palavra(palavra):
    # Converta a palavra em uma lista de caracteres
    palavra = list(palavra)
    
    # Crie uma lista para armazenar os caracteres embaralhados
    palavra_embaralhados = [''] * len(palavra)
    
    for i, p in enumerate(palavra):
        # Use uma fórmula matemática simples para calcular a nova posição
        # (i + 3) % len(palavra)
        #
        # i: índice original do caractere na palavra
        # +3: deslocamento fixo que estamos aplicando ao índice
        # % len(palavra): garante que a nova posição esteja dentro dos limites da lista
        #
        # Exemplo:
        # Se len(palavra) = 7 e o índice i = 4
        # Nova posição = (4 + 3) % 7 = 7 % 7 = 0
        #
        # Isso significa que o caractere que estava na posição 4 será movido para a posição 0
        nova_posicao = (i + 3) % len(palavra)
        
        # Coloca o caractere na nova posição calculada
        palavra_embaralhados[nova_posicao] = p
    
    # Junte os caracteres embaralhados de volta em uma string
    return ''.join(palavra_embaralhados)

palavra = input("Digite sua palavra: ")
palavra_embaralhada = embaralhar_palavra(palavra)
print("Palavra embaralhada:", palavra_embaralhada)


"""
Entrada Inicial: exemplo

    Deslocamento de 1:
    e (0) vai para (0 + 1) % 7 = 1
    x (1) vai para (1 + 1) % 7 = 2
    e (2) vai para (2 + 1) % 7 = 3
    m (3) vai para (3 + 1) % 7 = 4
    p (4) vai para (4 + 1) % 7 = 5
    l (5) vai para (5 + 1) % 7 = 6
    o (6) vai para (6 + 1) % 7 = 0
    
"""















