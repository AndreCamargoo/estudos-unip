"""
Exercício 2: Implemente uma função que recebe um número e retorna o nome do dia da semana
correspondente (usando uma simulação de switch).
"""
dia = int(input("Informe o dia da semana (1 a 7): "))

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido. Por favor, informe um número de 1 a 7.")

