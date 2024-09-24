#include <iostream>
#include <locale.h>

using namespace std;

int main() {
    float peso, altura, imc;

    setlocale(LC_ALL, "portuguese");

    for (int i = 0; i < 1; i++) {
        cout << "Digite seu peso: ";
        cin >> peso;

        cout << "Digite sua altura: ";
        cin >> altura;

        imc = peso / (altura * altura);

        cout << "Seu IMC é: " << imc << " - ";

        if (imc <= 18.5) {
            cout << "Magreza" << endl;
        } else if (imc <= 24.9) {
            cout << "Peso normal" << endl;
        } else if (imc <= 29.9) {
            cout << "Obesidade de grau I" << endl;
        } else if (imc <= 34.9) {
            cout << "Obesidade de grau II" << endl;
        } else {
            cout << "Obesidade de grau III" << endl;
        }
    }

    return 0;
}
