# Função para calcular a raiz quadrada usando o método de aproximação


def raiz_quadrada(num, precisao=0.0001):
    if num < 0:
        """
            A expressão raise é usada para gerar uma exceção.
            
            Exceções Integradas Comuns 
            
            ValueError
            - Indica que uma função recebeu um argumento com um valor adequado, mas com um tipo ou valor inadequado.
            - Exemplo: raise ValueError("Mensagem de erro")
            
            TypeError
            - Sinaliza que uma operação ou função foi aplicada a um objeto de tipo inadequado.
            - Exemplo: raise TypeError("Mensagem de erro")
            
            IndexError
            - Ocorre quando você tenta acessar um índice que está fora do intervalo válido de uma lista ou outra estrutura de dados indexada.
            - Exemplo: raise IndexError("Mensagem de erro")
            
            KeyError
            - Levantado quando uma chave não é encontrada em um dicionário.
            - Exemplo: raise KeyError("Mensagem de erro")
            
            FileNotFoundError
            - Ocorre quando você tenta abrir um arquivo que não existe.
            - Exemplo: raise FileNotFoundError("Mensagem de erro")
            
            ZeroDivisionError
            - Levantado quando uma divisão por zero é tentada.
            - Exemplo: raise ZeroDivisionError("Mensagem de erro")
            
            AttributeError
            - Sinaliza que um objeto não possui o atributo especificado.
            - Exemplo: raise AttributeError("Mensagem de erro")
            
            RuntimeError
            - Usado para erros que não se encaixam em outras categorias mais específicas.
            - Exemplo: raise RuntimeError("Mensagem de erro")
        """
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
    if num == 0:
        return 0
    
    estimativa = num
    
    # abs() retorna o valor absoluto de um número é a sua magnitude sem considerar o sinal, ou seja, é o número em sua forma não-negativa.
    
    """
        Detalhar o cálculo da raiz quadrada de 8 usando o método de aproximação de Newton-Raphson.
        Seguir as iterações do cálculo com a estimativa inicial e mostrar os cálculos detalhados
        
        Supondo que a estimativa é: 8
        
        Iteração 1
            Calcular o quadrado da estimativa:        
                8x8=64
            Calcular a diferença absoluta:
                abs(64-8)=abs(56)=56
            A diferença (56) é maior que a precisão (0.0001), então continuamos.
        
        Iteração 2
            Estimativa: 4.5
            Calcular o quadrado da estimativa:
                4.5x4.5=20.25
            Calcular a diferença absoluta:
                abs(20.25-8)=abs(12.25)=12.25
            A diferença (12.25) é maior que a precisão (0.0001), então continuamos.
        
        Iteração 3
            Estimativa: aproximadamente 3,138888888888889
            Calcular o quadrado da estimativa:
                3,138888888888889*3,138888888888889≈9,852623456790124
            Calcular a diferença absoluta:
                abs(9,852623456790124-8)=abs(1.86)=1,852623456790124
            A diferença (1.86) é maior que a precisão (0.0001), então continuamos.
        
        Iteração 4
            Estimativa: aproximadamente 2,826775
            Calcular o quadrado da estimativa:
                2,826775*2,826775≈8.0000
            Calcular a diferença absoluta:
                abs(8.0000-8)=abs(0.0000)=0.0000
            A diferença (0.0000) é menor que a precisão (0.0001), então o loop para.
    """
    while abs(estimativa * estimativa - num) > precisao:
        """
            Iteração 1
                Atualizar a estimativa:
                    nova_estimativa=(8+8/8)/2
                Primeiro, calcule a divisão
                    8/8=1
                Então
                    nova_estimativa=(8+1)/2
                Primeiro, some
                    8+1=9
                Então
                    9/2=4.5
                retorna estimativa
                
            Iteração 2
                Atualizar a estimativa:
                   nova_estimativa=(4.5+8/4.5)/2
                Primeiro, calcule a divisão
                    8/4.5≈1.7778
                Então
                    nova_estimativa=(4.5+1.7778)/2
                Primeiro, some
                    4.5+1.7778=6.2778
                Então
                    6.2778/2=3.1389
                retorna estimativa 
                     
            Iteração 3
                Atualizar a estimativa:
                    nova_estimativa=(3.1389+8/3.1389)/2
                Primeiro, calcule a divisão
                    8/3.1389≈2.548
                Então
                    nova_estimativa=(3.1389+2.548)/2
                Primeiro, some
                    3.1389+2.548=5.6869
                Então
                    5.6869/2=2.8435
                retorna estimativa
                
            Iteração 4
                Atualizar a estimativa:
                    nova_estimativa=(2.8435+8/2.8435)/2
                Primeiro, calcule a divisão
                    8/2.8435≈2.81
                Então
                    nova_estimativa=(2.8435+2.81)/2
                Primeiro, some
                    2.8435+2.81=5.6535
                Então
                    5.6535/2≈2.8268
                A diferença é menor que a precisão, então o loop para.
        """
        estimativa = (estimativa + num / estimativa) / 2
        
    return estimativa


# Recebendo as coordenadas dos pontos
xb = int(input("Digite o ponto xb: "))
xa = int(input("Digite o ponto xa: "))
yb = int(input("Digite o ponto yb: "))
ya = int(input("Digite o ponto ya: "))


# Calculando a distância
delta_x = xb - xa  # Exemplo: xb = 0, xa = 2 -> delta_x = 0 - 2 = -2
delta_y = yb - ya  # Exemplo: yb = 3, ya = 5 -> delta_y = 3 - 5 = -2


# Calculando a distância ao quadrado entre os pontos
distancia_quadrada = delta_x**2 + delta_y**2  # Exemplo: (-2)² + (-2)² = 4 + 4 = 8


# Calculando a raiz quadrada da distância ao quadrado para obter a distância
distancia = raiz_quadrada(distancia_quadrada)
"""
    Detalhamento do cálculo:
    Suponha que a distância ao quadrado entre os pontos seja armazenada na variável 'distancia_quadrada'.
    Por exemplo, se 'distancia_quadrada' é 8, isso significa que a distância ao quadrado entre os pontos é 8 unidades quadradas.
    A função raiz_quadrada(num, precisao) calcula a raiz quadrada de 'num' usando o método de aproximação de Newton-Raphson.

    No cálculo da raiz quadrada:
    1. Começamos com uma estimativa inicial que é o valor de 'num', ou seja, 'estimativa = distancia_quadrada'.
    2. Iteramos repetidamente até que o quadrado da estimativa se aproxime de 'num' dentro da precisão especificada:
       - Calculamos a nova estimativa como a média da estimativa atual e o valor de 'num' dividido pela estimativa atual.
       - A fórmula usada é: estimativa = (estimativa + num / estimativa) / 2
    3. O processo é repetido até que a diferença absoluta entre 'estimativa * estimativa' e 'num' seja menor ou igual à precisão desejada.
    4. A estimativa final fornece a raiz quadrada aproximada de 'num', que neste caso é a raiz quadrada de 'distancia_quadrada'.

    # Por exemplo, se 'distancia_quadrada' = 8, a raiz quadrada de 8 (aproximadamente 2.828) será calculada e armazenada em 'distancia'.
"""


# Exibindo o resultado
print(f"A distância entre os pontos é: {distancia}")  # Exibindo a distância formatada com 2 casas decimais

"""
    A diferença entre o resultado da sua calculadora e o resultado do seu código pode ser explicada por alguns fatores relacionados à 
    precisão e ao método utilizado para calcular a raiz quadrada
    
    1. Precisão e Arredondamento
    
        Calculadora: A maioria das calculadoras exibe números com uma precisão limitada. Portanto, a raiz quadrada de 8 pode ser 
        arredondada para um número com menos casas decimais, como 2,82842712474619.
        
        Código Python: 
            - O meu código usa o método de aproximação de Newton-Raphson, que pode fornecer um resultado com mais casas decimais do que a calculadora, 
            especialmente se a precisão especificada for muito pequena. 
            
            - O resultado que você obteve, 2.8284271250498643, tem mais casas decimais porque o método de aproximação é iterativo e precisa atender a
            uma condição de precisão, mas pode produzir uma quantidade maior de dígitos significativos.
            
    2. Método de Aproximação

        O método de Newton-Raphson (ou método da bisseção) utilizado no código calcula a raiz quadrada com uma precisão muito alta até atingir o critério de parada. 
        Isso significa que, mesmo que o valor exato seja um pouco diferente, o método pode gerar mais dígitos significativos.
        
    3. Comparação com math.sqrt

        Comparar com a precisão fornecida pela biblioteca padrão de Python, você pode usar math.sqrt(), que deve fornecer um valor com uma precisão similar à calculadora.
"""


