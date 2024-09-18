Algoritmo "André Camargo"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Este algoritmo calcula um código baseado na idade e no grupo.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/09/2024
Var
    idade: inteiro
    grupo: caracter

Inicio
    escreva("Digite sua idade: ")
    leia(idade)
    escreva("Digite o grupo (b, c, d, etc.): ")
    leia(grupo)


    SE (idade >= 18) E (idade <=70) ENTÃO

       SE (grupo = "b") OU (grupo = "B") ENTÃO
             SE (idade >= 18) E (idade <= 24) ENTÃO
                ESCREVA("Código 7")
                
                SENÃO
                     SE (idade >= 25) E (idade <= 40) ENTÃO
                        ESCREVA("Código 4")
                        
                        SENÃO
                             SE (idade >= 41) E (idade <= 70) ENTÃO
                                ESCREVA("Código 1")
                             FIMSE
                     FIMSE
             FIMSE

          SENÃO
             SE (grupo = "m") OU (grupo = "M") ENTÃO
                SE (idade >= 18) E (idade <= 24) ENTÃO
                   ESCREVA("Código 8")

                   SENÃO
                        SE (idade >= 25) E (idade <= 40) ENTÃO
                           ESCREVA("Código 5")

                           SENÃO
                                SE (idade >= 41) E (idade <= 70) ENTÃO
                                   ESCREVA("Código 2")
                                FIMSE
                        FIMSE
                FIMSE

                SENÃO
                   SE (grupo = "a") OU (grupo = "A") ENTÃO
                      SE (idade >= 18) E (idade <= 24) ENTÃO
                         ESCREVA("Código 9")

                         SENÃO
                              SE (idade >= 25) E (idade <= 40) ENTÃO
                                 ESCREVA("Código 6")

                                 SENÃO
                                      SE (idade >= 41) E (idade <= 70) ENTÃO
                                         ESCREVA("Código 3")
                                      FIMSE
                              FIMSE
                      FIMSE

                   SENÃO
                        ESCREVA("NÃO ENCONTADO O GRUPO")
                   FIMSE
             FIMSE
       FIMSE
    SENÃO
        escreva("Você não tem idade para adquirir um seguro")
    FIMSE
Fimalgoritmo