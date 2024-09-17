Algoritmo "Nota ponderada - Exercicio 1"
// Seção de Declarações das variáveis
Var
   n1, n2, n3, mp: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreva("Digite sua primeira nota: ")
   leia(n1)
   escreva("Digite sua segunda nota: ")
   leia(n2)
   escreva("Digite sua terceira nota: ")
   leia(n3)

   mp <- ( (n1*2) + (n2*3) + (n3*5) ) / (2 + 3 + 5)
   
   SE (mp >= 8) E (mp <=10) ENTAO
      escreva("Sua nota foi entre 8 e 10")
   SENAO
      SE (mp >= 7) E (mp <8) ENTAO
         escreva("Sua nota foi entre 7 e menor que 8")
      SENAO
         SE (mp >= 6) E (mp <7) ENTAO
            escreva("Sua nota foi entre 7 e menor que 7")
         SENAO
            SE (mp >= 5) E (mp <6) ENTAO
               escreva("Sua note foi entre 5 e menor que 6")
            SENAO
               escreva("xSua nota foi abaixo de 5")
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo


