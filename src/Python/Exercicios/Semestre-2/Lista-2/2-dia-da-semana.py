dia = int(input("Informe o dia da semana (1 a 7): "))

if 1 <= dia <= 7:
    match(dia):
        case 1:
            print('Segunda-Feira')
        case 2:
            print('Terça-Feira')
        case 3:
            print('Quarta-Feira')
        case 4:
            print('Quinta-Feira')
        case 5:
            print('Sexta-Feira')
        case 6:
            print('Sábado')
        case 7:
            print('Domingo')
else:
    print('Número inválido! Por favor, digite um número de 1 a 7.')