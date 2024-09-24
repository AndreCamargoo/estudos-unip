#include <iostream>
#include <locale.h>
#include <windows.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "portuguese");

    int vereador1 = 0;
    int vereador2 = 0;
    int prefeito1 = 0;
    int prefeito2 = 0;
    int votoVereadorBranco = 0;
    int votoVereadorNulo = 0;
    int votoPrefeitoBranco = 0;
    int votoPrefeitoNulo = 0;

    bool inicioVotacao = true;
    int qtdVotos = 0;

    int menu = 0;
    int menuVereador = 0;
    int menuPrefeito = 0;

    int encerrar = 0;

    while (inicioVotacao)
    {
        cout << "*************************" << endl;
        cout << "* 1 - Iniciar Votação   *" << endl;
        cout << "* 2 - Exibir Resultados *" << endl;
        cout << "* 3 - Encerrar Programa *" << endl;
        cout << "* Escolha uma opção:    *" << endl;
        cout << "*************************" << endl;
        cin >> menu;

        switch (menu)
        {
        case 1:
            system("cls");

            cout << "** Qual VEREADOR deseja votar? **" << endl;
            cout << "*  1 - Vereador 1               *" << endl;
            cout << "*  2 - Vereador 2               *" << endl;
            cout << "*  0 - Voto Branco              *" << endl;
            cout << "*********************************" << endl;
            cin >> menuVereador;

            switch (menuVereador)
            {
            case 1:
                vereador1++;
                break;
            case 2:
                vereador2++;
                break;
            case 0:
                votoVereadorBranco++;
                break;
            default:
                cout << "Opção de voto inválida!" << endl;
                votoVereadorNulo++;
                break;
            }

            system("cls");

            cout << "** Qual PREFEITO deseja votar? **" << endl;
            cout << "*  1 - Prefeito 1               *" << endl;
            cout << "*  2 - Prefeito 2               *" << endl;
            cout << "*  0 - Voto Branco              *" << endl;
            cout << "*********************************" << endl;
            cin >> menuPrefeito;

            switch (menuPrefeito)
            {
            case 1:
                prefeito1++;
                break;
            case 2:
                prefeito2++;
                break;
            case 0:
                votoPrefeitoBranco++;
                break;
            default:
                votoPrefeitoNulo++;
                break;
            }

            qtdVotos++;  // Incrementa o total de votos

            system("cls");
            cout << "FIM" << endl;
            Sleep(3000);
            system("cls");
            break;

        case 2:
            system("cls");

            if (qtdVotos == 0) {
                cout << "Nenhum voto registrado ainda." << endl;
            }
            else {
                // Vereador
                float totalVotosBrancosVereador = (votoVereadorBranco * 100.0) / qtdVotos;
                float totalVotosNulosVereador = (votoVereadorNulo * 100.0) / qtdVotos;

                // Prefeito
                float totalVotosBrancosPrefeito = (votoPrefeitoBranco * 100.0) / qtdVotos;
                float totalVotosNulosPrefeito = (votoPrefeitoNulo * 100.0) / qtdVotos;

                cout << "A quantidade de votos obtidos foi de: " << qtdVotos << endl << endl << endl;

                // Vereador

                cout << "A quantidade de votos em brancos para Vereadores é: " << votoVereadorBranco << endl;
                cout << "O percentual de votos em branco para Vereadores é: " << totalVotosBrancosVereador << "%" << endl << endl;

                cout << "A quantidade de votos em nulos para Vereadores é: " << votoVereadorNulo << endl;
                cout << "O percentual de votos nulos para Vereadores é: " << totalVotosNulosVereador << "%" << endl << endl;

                cout << "O vereador 1 obteve um total de " << vereador1 << " votos" << endl;
                cout << "O vereador 2 obteve um total de " << vereador2 << " votos" << endl << endl;

                // Prefeito
                cout << "A quantidade de votos em brancos para Prefeito é: " << votoPrefeitoBranco << endl;
                cout << "O percentual de votos em branco para Vereadores é: " << totalVotosBrancosPrefeito << "%" << endl << endl;

                cout << "A quantidade de votos em nulos para Vereadores é: " << votoPrefeitoNulo << endl;
                cout << "O percentual de votos nulos para Vereadores é: " << totalVotosNulosPrefeito << "%" << endl << endl;

                cout << "O prefeito 1 obteve um total de " << prefeito1 << " votos" << endl;
                cout << "O prefeito 2 obteve um total de " << prefeito2 << " votos" << endl << endl;
            }

            Sleep(3000);

            cout << "** Deseja continuar voltando    **" << endl;
            cout << "*  1 - Sim                       *" << endl;
            cout << "*  2 - Não, encerrar o programa  *" << endl;
            cout << "*  Escolha uma opção:            *" << endl;
            cout << "**********************************" << endl;
            cin >> encerrar;

            if (encerrar == 2) {
                inicioVotacao = false;
            }

            break;

        case 3:
            inicioVotacao = false;
            break;

        default:
            cout << "Informe a opção desejada conforme o menu apresentado" << endl;
            continue;
        }

        cout << "Quantidade de votos: " << qtdVotos << endl;
    }

    return 0;
}