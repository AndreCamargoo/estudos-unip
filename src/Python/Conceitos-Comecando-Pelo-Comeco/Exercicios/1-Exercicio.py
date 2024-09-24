'''

    Exercício
    
    Peça ao usuário para digitar seu nome
    Peça ao usuário para digitar sua idade
    
    Se nome e idade forem digitado
        Exiba:
            Seu nome é {nome}:
            Seu nome invertido é {nome invertido} :
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digigado em nome ou idade:
        Exiba:
            Desculpe, você deixou os campos vazios

'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('-'*50)
    
    print(f'Seu nome invertido é {nome[::-1]}')
    print('-'*50)
    
    if ' ' in nome:
        print('Seu nome contém espaços')
        print('-'*50)
    else:
         print('Seu nome não contém espaços')
         print('-'*50)
         
    print(f'Seu nome tem {len(nome)} letras')
    print('-'*50)
    
    print(f'A primeira letra do seu nome é {nome[0]}')
    print('-'*50)
    
    print(f'A última letra do seu nome é {nome[-1]}')
    print('-'*50)
else:
    print('Desculpe, você deixou os campos vazios')