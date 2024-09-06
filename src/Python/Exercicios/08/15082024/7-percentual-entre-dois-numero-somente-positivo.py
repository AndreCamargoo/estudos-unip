# Função para verificar se o número informado é positivo
def obter_numero_positivo(prompt):
    """
        O loop while True é uma construção comum para criar um loop que continua indefinidamente até que uma condição de término seja atendida.
        
        Início do Loop Infinito:
            - O while True inicia um loop que nunca termina por conta própria, o que significa que o código dentro do loop será executado 
            repetidamente até que uma condição de término explícita seja encontrada (neste caso, um return ou um break).
            
        Solicitação e Conversão da Entrada:
            - Solicita a Entrada: O input(prompt) pede ao usuário para inserir um valor com a mensagem fornecida no prompt.
            - Conversão para float: Tenta converter a entrada do usuário para um número decimal (float). Se a entrada não puder ser convertida, 
            o ValueError será acionado
            
        Validação do Número:
            - Número Negativo: Se o número convertido é negativo (numero < 0), uma mensagem de erro é exibida, e o loop continua 
            para solicitar uma nova entrada.
            - Número Válido: Se o número não for negativo, o loop é encerrado com o comando return numero, que retorna o número 
            válido ao ponto de chamada da função.
            
        Tratamento de Erros:
            - Exceção ValueError: Se a entrada não puder ser convertida para float (por exemplo, se o usuário digitar texto não numérico), 
            o bloco except captura a exceção e exibe uma mensagem de erro, solicitando uma nova entrada.
    """
    while True:
        try:
            # Solicita a entrada do usuário e tenta converter para float
            numero = float(input(prompt))
            if numero < 0:
                # Se o número for negativo, exibe uma mensagem de erro e solicita novamente
                print("Erro: O número não pode ser negativo. Tente novamente.")
            else:
                # Retorna o número se ele for positivo
                return numero
        except ValueError:
            # Captura erro se a entrada não puder ser convertida para float
            print("Entrada inválida. Por favor, insira um número válido.")

# Solicitar a entrada de dois números positivos do usuário
n1 = obter_numero_positivo("Digite seu 1º número: ")
n2 = obter_numero_positivo("Digite seu 2º número: ")

# Calcular o percentual de n1 em relação a n2
if n2 == 0:
    # Verifica se o divisor é zero para evitar divisão por zero
    print("Erro: Divisão por zero não é permitida.")
else:
    # Calcula o percentual de n1 em relação a n2
    percentual = (n1 / n2) * 100
    # Exibe o resultado formatado com duas casas decimais
    print(f"O percentual é de: {percentual:.2f}%")
