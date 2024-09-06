"""
    Variáveis de ambiente

    Variáveis de ambiente são valores que você define fora do código, geralmente no sistema operacional ou
    em arquivos de configuração, como credenciais de banco de dados, URLs de API, ou configurações específicas
    do sistema.
"""

import os

# Definindo Variáveis Locais:
# Definidas dentro do código Python.
# Só existem enquanto o código está sendo executado.
# Usadas para armazenar dados temporários ou intermediários necessários durante a execução do código.
nome = 'André Camargo'
print(nome)

# Acessando uma variável de ambiente
# Certifique-se de que a variável de ambiente 'MINHA_VARIAVEL' está definida no seu sistema
variavel_ambiente = os.getenv('MINHA_VARIAVEL', 'Valor padrão para variável de ambiente')
print(variavel_ambiente)

# Considerações Adicionais
# Segurança: Use variáveis de ambiente para armazenar informações sensíveis como senhas e chaves de API.
# Isso evita que essas informações fiquem expostas no código-fonte.
#
# Portabilidade: Usar variáveis de ambiente torna seu código mais flexível e adaptável a diferentes ambientes,
# como desenvolvimento, teste e produção.