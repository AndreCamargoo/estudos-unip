Algoritmo "IMC"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 05/09/2024
Var
peso, altura, imc: real


Inicio

escreval("Informe seu peso")
leia(peso)
escreval("Informe sua altura")
leia(altura)

imc <- peso / (altura*altura)

SE (imc <= 18.5) ENTAO
escreva("Magreza")
   SENAO
      SE (imc >= 18.6) E (imc < 24.9) ENTAO
         escreva("Peso normal")
   SENAO
         SE (imc >= 25) E (imc <= 29.9) ENTAO
            escreva("Sobrepeso")
         SENAO
              SE (imc >= 30) E (imc < 34.9) ENTAO
                 escreva("Obesidade de grau l")
              SENAO
                   SE (imc >= 35) E (imc <= 39.9) ENTAO
                      escreva("Obesidade de grau ll")
                   SENAO
                        escreva("Obesidade de grau lll")
                   FIMSE
              FIMSE
         FIMSE
   FIMSE
FIMSE

Fimalgoritmo