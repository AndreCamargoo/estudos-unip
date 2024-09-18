def vogal(palavra):
    vogais = 'aeiou'
    primeiro_caractere = palavra[0].lower()
    resultado = primeiro_caractere in vogais
    return resultado


def analiseTexto(texto, palavra_especifica):
    palavras = texto.split()
    total_palavras = len(palavras)
    contaPalavras = palavras.count(palavra_especifica)
    palavrasVogal = sum(1 for palavra in palavras if vogal(palavra))

    if total_palavras > 0:
        percentual = (palavrasVogal / total_palavras) * 100
    else:
        percentual = 0.0

    return total_palavras, contaPalavras, percentual

frase = input("Digite o texto: ")
palavraEspecifica = input("Digite a palavra específica que deseja contar: ")


total_palavras, ocorrencias_palavra, percentual_vogais = analiseTexto(frase, palavraEspecifica)

print(f"Número total de palavras: {total_palavras}")
print(f"Número de ocorrências da palavra '{palavraEspecifica}': {ocorrencias_palavra}")
print(f"Percentual de palavras que começam com vogal: {percentual_vogais:.2f}%")