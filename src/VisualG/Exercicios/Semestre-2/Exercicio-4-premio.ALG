Algoritmo "Andr� Camargo"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/09/2024
Var
// Se��o de Declara��es das vari�veis 
horasExtras, horasFalta, premio: real

Inicio

escreva("Informe as horas extras: ")
leia(horasExtras)
escreva("Informe as horas falta: ")
leia(horasFalta)

premio <- (horasExtras*60) - (2/3 * (horasFalta*60))

SE (premio > 2400) ENT�O
   ESCREVA("Seu premio ser� de R$ 500")
   
   SEN�O
        SE (premio >= 1800) E (premio < 2400) ENT�O
           ESCREVA("Seu premio ser� de R$ 400")
           
           SEN�O
                SE (premio >= 1200) E (premio < 1800) ENT�O
                   ESCREVA("Seu premio ser� de R$ 300")
                   
                   SEN�O
                        SE (premio >= 600) E (premio < 1200) ENT�O
                           ESCREVA("Seu premio ser� de R$ 200")
                        SEN�O
                             escreva("Seu premio ser� de R$ 100")
                        FIMSE
                FIMSE
        FIMSE
FIMSE

Fimalgoritmo