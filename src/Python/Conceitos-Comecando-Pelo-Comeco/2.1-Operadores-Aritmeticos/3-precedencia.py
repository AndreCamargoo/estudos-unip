"""
    Os operadores em Python seguem uma ordem de precedência que determina a sequência em que as operações são realizadas:

    Parênteses ( ) - Alteram a ordem natural de precedência.
    Exponenciação ** - Potência.
    Multiplicação *, Divisão /, Divisão inteira //, e Módulo % - Operações aritméticas.

"""

# O cálculo é feito com base na precedência dos operadores
resultado = 1 + 1 ** 5 + 5
print(resultado) # 7

# Corrigindo a precedência com parênteses para a ordem desejada
resultado_correto = (1 + 1) ** (5 + 5)
print(resultado_correto) # int 1024

resultado2 = (1 + (0.5 + 0.5)) ** (5 + 5)
print(resultado2) # float 1024.0

resultado3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(resultado3) # int 1024



