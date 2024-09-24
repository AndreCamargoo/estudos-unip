"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite seu número: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('número é par')
    else:
        print('número é ímpar')
else:
    print('número digitado não e um inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite o horario: ')

if hora.isdigit():
    hora = int(hora)
    match hora:
        case _ if 1 <= hora <= 11:
            print('Bom dia')
        case _ if 12 <= hora <= 17:
            print('Boa tarde')
        case _ if 18 <= hora <= 23:
            print('Boa noite')
        case _:
            print('Hora desconhecida')
else:
    print('Horario não foi informado')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')

if len(nome) > 3:
    
    match nome:
        case _ if len(nome) <= 4:
            print('Seu nome é muito curto')
        case _ if 5 <= len(nome) <= 6:
            print('Seu nome é normal')
        case _:
            print('Seu nome é muito grande')
else:
    print('Informe um nome com no minimo 3 caracteres')