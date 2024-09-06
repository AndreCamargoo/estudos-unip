"""

    Os operadores lógicos são ferramentas fundamentais na programação e na computação, pois permitem combinar e manipular valores booleanos, 
    que são representações de verdade e falsidade. Em termos simples, um computador opera exclusivamente com valores binários, 
    ou seja, TRUE (Verdadeiro) e FALSE (Falso), que são representados por 1 e 0, respectivamente.

    Os operadores lógicos, como AND, OR e NOT, são usados para realizar operações sobre esses valores booleanos. Por exemplo:

    AND (E): O resultado é TRUE apenas se ambos os operandos forem TRUE.
    OR (OU): O resultado é TRUE se pelo menos um dos operandos for TRUE.
    NOT (NÃO): Inverte o valor do operando; TRUE torna-se FALSE e vice-versa.
    
    Esses operadores ajudam a construir condições e decisões dentro dos programas, tornando-os capazes de realizar tarefas complexas baseadas em lógica.

"""

a = True
b = False

if a and b: # A e B são verdadeiros
    print('Atendeu a condição')
    
else:
    print('Não atendeu a condição')


if a or b: # A ou B é verdadeiro
    print('Atendeu a condição')
    
else:
    print('Não atendeu a condição')

idade = 27
nome = 'André'

if idade <= 25:
    print('Está na melhor idade')
elif idade >=25 and idade < 30:
    print('As contas te pegaram, fu....')
else:
    print('Vivemos para trabalhar')


if not nome:
    print('Nome não foi informado')
else:
    print(f'Meu nome é {nome}')