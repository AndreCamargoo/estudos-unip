Algoritmo "André Camargo"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/09/2024
Var
// Seção de Declarações das variáveis 
horasExtras, horasFalta, premio: real

Inicio

escreva("Informe as horas extras: ")
leia(horasExtras)
escreva("Informe as horas falta: ")
leia(horasFalta)

premio <- (horasExtras*60) - (2/3 * (horasFalta*60))

SE (premio > 2400) ENTÃO
   ESCREVA("Seu premio será de R$ 500")
   
   SENÃO
        SE (premio >= 1800) E (premio < 2400) ENTÃO
           ESCREVA("Seu premio será de R$ 400")
           
           SENÃO
                SE (premio >= 1200) E (premio < 1800) ENTÃO
                   ESCREVA("Seu premio será de R$ 300")
                   
                   SENÃO
                        SE (premio >= 600) E (premio < 1200) ENTÃO
                           ESCREVA("Seu premio será de R$ 200")
                        SENÃO
                             escreva("Seu premio será de R$ 100")
                        FIMSE
                FIMSE
        FIMSE
FIMSE

Fimalgoritmo