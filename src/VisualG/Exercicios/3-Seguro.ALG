algoritmo "Seguro_Categorias"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
var
    idade: inteiro
    grupo_risco: caractere
    codigo_seguro: inteiro
    linha, coluna: inteiro
    matriz_grupos_risco: vetor[1..3,1..3] de inteiro
inicio
    // Inicializando a matriz com os códigos de seguro
    matriz_grupos_risco[1,1] <- 7  // Baixo, 18-24
    matriz_grupos_risco[1,2] <- 8  // Médio, 18-24
    matriz_grupos_risco[1,3] <- 9  // Alto, 18-24

    matriz_grupos_risco[2,1] <- 4  // Baixo, 25-40
    matriz_grupos_risco[2,2] <- 5  // Médio, 25-40
    matriz_grupos_risco[2,3] <- 6  // Alto, 25-40

    matriz_grupos_risco[3,1] <- 1  // Baixo, 41-70
    matriz_grupos_risco[3,2] <- 2  // Médio, 41-70
    matriz_grupos_risco[3,3] <- 3  // Alto, 41-70

    // Entrada de dados
    escreva("Digite a idade (entre 18 e 70): ")
    leia(idade)
    escreva("Digite o grupo de risco (b para baixo, m para médio, a para alto): ")
    leia(grupo_risco)

    // Verificação da idade
    se (idade >= 18) e (idade <= 70) entao
        // Determinação da faixa etária (linha da matriz)
        se (idade >= 18) e (idade <= 24) entao
            linha <- 1
        senao
            se (idade >= 25) e (idade <= 40) entao
                linha <- 2
            senao
                se (idade >= 41) e (idade <= 70) entao
                    linha <- 3
                fimse
            fimse
        fimse

        // Determinação do grupo de risco (coluna da matriz)
        se grupo_risco = "b" entao
            coluna <- 1
        senao
            se grupo_risco = "m" entao
                coluna <- 2
            senao
                se grupo_risco = "a" entao
                    coluna <- 3
                fimse
            fimse
        fimse

        // Acessando o código de seguro
        codigo_seguro <- matriz_grupos_risco[linha, coluna]

        // Exibindo o código de seguro
        escreval("O código do seguro é: ", codigo_seguro)

    senao
        escreval("Idade fora do intervalo permitido.")
    fimse
fimalgoritmo
