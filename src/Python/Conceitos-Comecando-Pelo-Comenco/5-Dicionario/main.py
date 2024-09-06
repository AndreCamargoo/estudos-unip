"""
    Dicionários: {key, value}
    
    Um dicionário em Python é uma estrutura de dados que armazena pares de chave-valor. 
    
    Ele é uma das várias estruturas de dados que o Python oferece, junto com listas, sets e tuplas, 
    cada uma com suas características e usos específicos.
    
    Lista: É uma coleção ordenada de itens, acessível por índices numéricos. 
    Os itens são armazenados na ordem em que foram adicionados e cada item pode ser acessado usando seu índice, 
    começando por 0. Por exemplo, para acessar o quarto item de uma lista, usamos 
    lista[3].
    
            ------------------- Posições ----------------------
    Valores | 10 | 14 | 20 | 9 | 16 | 22 | 58 | 64 | 70 | 102 | 
            ---------------------------------------------------
    Índices | 0  |  1 |  2 | 3 |  4 |  5 |  6 |  7 |  8 |  9  |
            ---------------------------------------------------
            
    Dicionário: É uma coleção não ordenada de pares chave-valor. Cada item é acessível através de uma chave única em vez de um índice numérico. 
    As chaves podem ser de qualquer tipo imutável, como strings ou números. Para acessar um valor, usamos a chave associada a ele, por exemplo, 
    dicionario['n10'].
    
            ------------------- Posições -----------------------
    Valores | 10 | 14 | 20 |  9 | 16 | 22 | 58 | 64 | 70 | 102 | 
            ----------------------------------------------------
    Chaves  | n1 | n2 | n3 | n4 | n5 | n6 | n7 | n8 | n9 | n10 |
            ----------------------------------------------------
"""

lista = [10,14,20,9,16,22,58,64,70,102]

for indice, valor in enumerate(lista):
    print(indice, valor)
    
print(lista[3])

# dicionario = dict() #ou
dicionario = {
    'n1': 10,
    'n2': 14,
    'n3': 20,
    'n4': 9,
    'n5': 16,
    'n6': 22,
    'n7': 58,
    'n8': 64,
    'n9': 70,
    'n10': 102
}

# Listar
print(dicionario)

# Listar um elemento especifico
print(dicionario['n10'])

# Usando método para acessar o dicionario
print(dicionario.get('n6'))

# Remover elementos dentro do dicionario
print(dicionario.pop('n6'))

print(dicionario)

# Listar todas as chaves do dicionario sem valores
print(dicionario.keys())

# Listar todas os do dicionario sem as chaves
print(dicionario.values())

# Limpar dicionario 
print(dicionario.clear())

pessoa = {
    'nome': 'André Camargo',
    'sexo': 'Masculino',
    'profissao': 'Dev',
    'interesses': [
        'Python',
        'Php',
        'Node',
        'React',
        'VueJs',
        'Angular'
    ], #array
    'pets': {
        'nome': 'Lua',
        'peso': 2.5,
        'idade': 4
    } # dicionário
}

print(pessoa)
print(pessoa.get('nome'))

#print(pessoa['interesses'])
#print(pessoa['interesses'][3])

print(pessoa.get('interesses'))
print(pessoa.get('interesses')[3])

#print(pessoa['pets'])
#print(pessoa['pets']['peso'])

print(pessoa.get('pets'))
print(pessoa.get('pets').get('peso'))

# Adicionar novo elemento dentro do dicionário
pessoa['ano_nascimento'] = 2000
print(pessoa)


"""
    append():

    Uso: Adiciona um único elemento ao final da lista.

    Sintaxe: lista.append(elemento)
"""

# Novo interesse que queremos adicionar
novo_interesse = 'Inteligência Artificial'
# Adicionar o novo interesse à lista existente usando o método append
pessoa['interesses'].append(novo_interesse)
print(pessoa)

"""
    extend():

    Uso: Adiciona vários elementos ao final da lista, a partir de um iterável (como uma lista, tupla, ou conjunto).

    Sintaxe: lista.extend(iteravel)
"""

# Novos interesses que queremos adicionar lista existente
novos_interesses = ['Docker', 'Kubernetes']

#Isso pode ser feito usando o método extend()
pessoa['interesses'].extend(novos_interesses)
print(pessoa)

"""
    insert()

    Uso: Adicionar um único elemento em uma posição específica

    Sintaxe: lista.insert(0, iteravel)
"""
pessoa['interesses'].insert(4, 'C++')
print(pessoa)

"""
    Operador +
    
    Uso: Pode criar uma nova lista com os elementos que deseja adicionar e concatená-la com a lista original

    Sintaxe: lista = lista + novos_elementos
"""
novos_elementos = ['C#', 'CSS']
pessoa['interesses'] = novos_elementos + pessoa['interesses']
print(pessoa)

pessoa['pets']['ano_nascimento'] = 2000
print(pessoa)
