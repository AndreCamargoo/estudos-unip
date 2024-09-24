#include <iostream>
#include <locale.h>

using namespace std;

int main() {
    float horasExtras, horasFalta, premio;
    char continuar;

    setlocale(LC_ALL, "portuguese");

    do {
        cout << "Digite as horas extras: ";
        cin >> horasExtras;

        cout << "Digite as horas faltas: ";
        cin >> horasFalta;

        cout << "Suas horas extras foram de: " << horasExtras * 60 << " minutos" << endl;
        cout << "Suas horas faltas foram de: " << horasFalta * 60 << " minutos" << endl;

        premio = (horasExtras * 60) - (2.0 / 3.0 * (horasFalta * 60));

        int premioCategoria;

        if (premio > 2400) {
            premioCategoria = 500;
        }
        else if (premio >= 1800) {
            premioCategoria = 400;
        }
        else if (premio >= 1200) {
            premioCategoria = 300;
        }
        else if (premio >= 600) {
            premioCategoria = 200;
        }
        else {
            premioCategoria = 100;
        }

        // Usando switch para exibir o pr�mio
        switch (premioCategoria) {
        case 500:
            cout << "Seu premio será de R$ 500" << endl;
            break;
        case 400:
            cout << "Seu premio será de R$ 400" << endl;
            break;
        case 300:
            cout << "Seu premio será de R$ 300" << endl;
            break;
        case 200:
            cout << "Seu premio será de R$ 200" << endl;
            break;
        case 100:
            cout << "Seu premio será de R$ 100" << endl;
            break;
        }

        cout << "Deseja calcular novamente? (s/n): ";
        cin >> continuar;

    } while (continuar == 's' || continuar == 'S');

    return 0;
}
