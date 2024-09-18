# Cálculo da área de um círculo
# Peça ao usuário para digitar o raio de um círculo e calcule a área. Fórmula da área é A=πr², onde π = 3.14159


"""
A=πr²

A -> é a área do círculo.
π -> (pi) é uma constante matemática aproximadamente igual a 3.14159.
r -> é o raio do círculo.
"""


raio = float(input("Digite o raio: "))  # Solicita ao usuário que insira o valor do raio
pi = 3.14159 # Valor de pi


area = pi * raio ** 2 # Calcula a área usando a fórmula A = πr²


print(f"O resultado é: {area}")  # Exibe a área calculada

"""
    Exemplo de Uso do Operador "**"
    
    Quadrado de um Número:
    
        Para calcular o quadrado de um número (ou seja, o número elevado à potência de 2), você usa o operador "**":
        
            x = 5
            quadrado = x ** 2
            print(quadrado)  # Saída: 25
"""