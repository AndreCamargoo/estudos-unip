Algoritmo "Andr� Camargo"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Este algoritmo calcula um c�digo baseado na idade e no grupo.
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


    SE (idade >= 18) E (idade <=70) ENT�O

       SE (grupo = "b") OU (grupo = "B") ENT�O
             SE (idade >= 18) E (idade <= 24) ENT�O
                ESCREVA("C�digo 7")
                
                SEN�O
                     SE (idade >= 25) E (idade <= 40) ENT�O
                        ESCREVA("C�digo 4")
                        
                        SEN�O
                             SE (idade >= 41) E (idade <= 70) ENT�O
                                ESCREVA("C�digo 1")
                             FIMSE
                     FIMSE
             FIMSE

          SEN�O
             SE (grupo = "m") OU (grupo = "M") ENT�O
                SE (idade >= 18) E (idade <= 24) ENT�O
                   ESCREVA("C�digo 8")

                   SEN�O
                        SE (idade >= 25) E (idade <= 40) ENT�O
                           ESCREVA("C�digo 5")

                           SEN�O
                                SE (idade >= 41) E (idade <= 70) ENT�O
                                   ESCREVA("C�digo 2")
                                FIMSE
                        FIMSE
                FIMSE

                SEN�O
                   SE (grupo = "a") OU (grupo = "A") ENT�O
                      SE (idade >= 18) E (idade <= 24) ENT�O
                         ESCREVA("C�digo 9")

                         SEN�O
                              SE (idade >= 25) E (idade <= 40) ENT�O
                                 ESCREVA("C�digo 6")

                                 SEN�O
                                      SE (idade >= 41) E (idade <= 70) ENT�O
                                         ESCREVA("C�digo 3")
                                      FIMSE
                              FIMSE
                      FIMSE

                   SEN�O
                        ESCREVA("N�O ENCONTADO O GRUPO")
                   FIMSE
             FIMSE
       FIMSE
    SEN�O
        escreva("Voc� n�o tem idade para adquirir um seguro")
    FIMSE
Fimalgoritmo