import random

saldo_atual = 0
especial = 200

contaDepositos = 0
contaSaques = 0

senha = ''
logado = True

mensagens_deposito = [
    "De grão em grão a galinha enche o papo!",
    "Mais dinheiro na conta, mais motivos para sorrir!",
    "Seu saldo está subindo como fermento em bolo!",
    "Seus depósitos estão fazendo seu saldo crescer como mágica!",
    "Cada centavo conta... e o seu saldo agradece!",
    "Você está enchendo o cofre mais rápido do que um furacão!",
    "Olha só, seu saldo está igual a um pão quentinho saindo do forno!",
    "Com cada depósito, seu saldo fica mais forte que café expresso!",
    "Seu dinheiro está crescendo mais rápido que uma planta no verão!",
    "Cada real que entra é um passo para a fortuna!"
]

mensagens_saque = [
    "Seu dinheiro voou, mas ainda temos alguns na conta!",
    "Parece que você está comprando um café expresso com esse saque!",
    "Seu saldo fez um buraco, mas ainda está firme!",
    "Você fez um saque, agora seu saldo está um pouco mais leve!",
    "Saiu um pouco do seu dinheiro, mas não se preocupe, ele volta logo!",
    "O saldo deu uma leve diminuída, mas nada que um novo depósito não cure!",
    "Saque realizado! Seu saldo está dando uma folguinha.",
    "Seu dinheiro saiu para uma pequena viagem, mas logo estará de volta!",
    "O saldo está respirando fundo após esse saque!",
    "Saque feito! Seu saldo está só um pouquinho mais cansado agora."
]

def mensagem_aleatoria(lista_mensagens):
    return random.choice(lista_mensagens)


conta = int(input('Informe o número da sua conta: \n'))

if conta:
    while logado:
        senha = int(input('Informe a senha:\n'))

        if senha == 123:
            print("Seja bem-vindo, André Camargo!")

            while senha:

                acao = int(input("Navegue pelo menu: \n "
                                 "1 para consultar saldo atual \n "
                                 "2 para realizar um depósito \n "
                                 "3 para realizar um saque \n "
                                 "4 para sair: \n"))

                match (acao):
                    case 1:
                        print(f"Seu saldo atual é: R$ {saldo_atual:.2f}\n")

                    case 2:
                        deposito = float(input('Informe o valor do depósito:\n'))
                        saldo_atual += deposito
                        print(f"Depósito realizado com sucesso. Seu saldo atual é: R$ {saldo_atual:.2f} ")
                        print(mensagem_aleatoria(mensagens_deposito)+"\n")

                    case 3:
                        sacar = float(input('Informe o valor do saque:\n'))

                        if saldo_atual >= sacar:
                            saldo_atual -= sacar
                            print(f"Saque de R$ {sacar:.2f} realizado com sucesso. Seu saldo atual é: "
                                  f"R$ {saldo_atual:.2f}\n")
                            print(mensagem_aleatoria(mensagens_saque) + "\n")
                        elif saldo_atual + especial >= sacar:
                            saldo_atual -= sacar
                            print(f"Saque de R$ {sacar:.2f} realizado com sucesso, utilizando seu crédito especial. "
                                  f"Seu saldo atual é: R$ {saldo_atual:.2f}\n")
                            print(mensagem_aleatoria(mensagens_saque) + "\n")
                        else:
                            print('Saldo insuficiente para o saque solicitado. Por favor, verifique seu saldo e o '
                                  'limite do crédito especial.\n')

                    case 4:
                        print("Você saiu da conta. Até mais!")
                        logado = False
                        senha = ''
        else:
            print('Senha informada é incorreta')