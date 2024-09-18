"""
    Exercício 4: Crie um loop while que continue pedindo ao usuário para inserir uma
    palavra até que ele insira "sair".
"""
palavras = {"palavra1", "palavra2", "palavra3", "palavra4", "palavra5", "sair"}
for palavra in palavras:
    if palavra == "sair":
        print("achei a palvra: ", palavra)


""" 
    Exercício 5: Escreva um código que utilize break para sair de um loop infinito quando um número 
    aleatório entre 1 e 10 seja igual a 7. 
"""
n = 0
while True:
    if n == 7:
        print("saindo do loop infinito")
        break
    n += 1

