Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/09/2024
Var

salario_minimo, horas_trabalhadas, horas_extras: real
dependentes: inteiro


valor_hora_trabalhada, salario_mes, valor_dependentes, valor_hora_extra: real
valor_horas_extras, salario_bruto, salario_final: real

irrf, salario_liquido, gratificacao: real

Inicio
escreval("Informe o valor do salário mínimo: R$")
leia(salario_minimo)

escreval("Informe o número de horas trabalhadas:")
leia(horas_trabalhadas)

escreval("Informe o número de dependentes:")
leia(dependentes)

escreval("Informe a quantidade de horas extras trabalhadas:")
leia(horas_extras)


valor_hora_trabalhada <- salario_minimo / 5
salario_mes <- horas_trabalhadas * valor_hora_trabalhada
valor_dependentes <- dependentes * 32.00
valor_hora_extra <- valor_hora_trabalhada * 1.5
valor_horas_extras <- horas_extras * valor_hora_extra

salario_bruto <- salario_mes + valor_dependentes + valor_horas_extras

SE (salario_bruto < 200)ENTAO
   irrf <- 0
SE
  SENAO (salario_bruto <= 500) ENTAO
        irrf <- salario_bruto * 0.10
  FIMSE
SENAO
     irrf <- salario_bruto * 0.20;
FIMSE

salario_liquido <- salario_bruto - irrf;

SE (salario_liquido <= 350) ENTAO
   gratificacao <- 100;
SENAO
     gratificacao <- 50;
FIMSE

salario_final <- salario_liquido + gratificacao;

escreval("Salário bruto: R$: ",salario_bruto)
escreval("IRRF: R$: ",irrf)
escreval("Salário líquido: R$: ",salario_liquido)
escreval("Gratificação: R$: ",gratificacao)
escreval("Salário final a receber: R$: ",salario_final)

Fimalgoritmo