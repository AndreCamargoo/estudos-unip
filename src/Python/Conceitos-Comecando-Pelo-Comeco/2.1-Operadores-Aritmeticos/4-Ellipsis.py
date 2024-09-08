"""
    Ellipsis Python
    
    Em Python, Ellipsis é um objeto especial representado por .... 
    Embora não seja utilizado com frequência em muitos códigos do dia a dia, possui algumas aplicações e significados importantes, principalmente em contextos específicos.
    
    Ellipsis é frequentemente usado como um marcador de posição em código. 
    Pode servir para indicar onde mais código deve ser adicionado no futuro ou para representar seções incompletas de uma implementação.
    
    Tem outras modos de uso também!
"""

print(type(...))  # <class 'ellipsis'>

# O ... (Ellipsis) é um objeto especial em Python, frequentemente utilizado como um marcador de posição. 
# Nesse contexto, o ... atua como um substituto para o código que ainda precisa ser escrito.
def minhaFuncao():
    ...

# O pass é uma instrução que não faz nada. 
# É um comando nulo em Python e é usado como um espaço reservado em blocos de código onde uma declaração é obrigatória, mas nenhuma ação é necessária.
def minhaFuncao2():
    pass
    
minhaFuncao()