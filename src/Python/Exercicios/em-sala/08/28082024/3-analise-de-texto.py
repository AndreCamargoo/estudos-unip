"""
    Análise de Texto
    Desenvolva um programa que analise um texto fornecido pelo usuário e forneça as seguintes informações:

    - O número total de palavras no texto.
    - O número de ocorrências de uma palavra específica, também fornecida pelo usuário.
    - O percentual de palavras que são vogais (palavras que começam com 'a', 'e', 'i', 'o' ou 'u').

    **Dicas:**

    - Use a função `len()` para obter o número total de palavras.
    - Utilize o método `.count()` para contar as ocorrências de uma palavra específica.
    - Crie uma função que receba uma palavra e retorne `True` se começar com uma vogal e `False` caso contrário.
    Essa função pode ser útil para calcular o percentual de palavras que são vogais.
"""
def vogal(palavra):
    """
        Retorna True se a palavra começa com uma vogal, False caso contrário.
    """

    #print(f"Palavra: {palavra}")
    #print(f"Primeiro caractere: {palavra[0]}")

    # Definição das vogais
    vogais = 'aeiou'

    # lower() - Verifica se o primeiro caractere (em minúsculo) está nas vogais
    primeiro_caractere = palavra[0].lower()
    print(f"Primeiro caractere em minúsculo: {primeiro_caractere}")

    resultado = primeiro_caractere in vogais
    print(f"Está nas vogais? {resultado}")

    return resultado


def analiseTexto(texto, palavra_especifica):
    """
        Analisa o texto e retorna o número total de palavras, o número de ocorrências da palavra específica e o
        percentual de palavras que começam com vogal.
    """
    # Quebra o texto em palavras
    palavras = texto.split()

    # Contagem total de palavras
    total_palavras = len(palavras)
    #print(total_palavras)

    # Contagem de ocorrências da palavra específica
    contaPalavras = palavras.count(palavra_especifica)
    #print(contaPalavras)

    # Contagem de palavras que começam com vogal
    palavrasVogal = sum(1 for palavra in palavras if vogal(palavra))
    #print(f"Total de palavras: {total_palavras}")

    # Percentual de palavras que começam com vogal
    if total_palavras > 0:
        percentual = (palavrasVogal / total_palavras) * 100
    else:
        percentual = 0.0

    return total_palavras, contaPalavras, percentual

frase = input("Digite o texto: ")
palavraEspecifica = input("Digite a palavra específica que deseja contar: ")


# Análise do texto
total_palavras, ocorrencias_palavra, percentual_vogais = analiseTexto(frase, palavraEspecifica)

print(f"Número total de palavras: {total_palavras}")
print(f"Número de ocorrências da palavra '{palavraEspecifica}': {ocorrencias_palavra}")
print(f"Percentual de palavras que começam com vogal: {percentual_vogais:.2f}%")