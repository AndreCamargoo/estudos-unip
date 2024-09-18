#include <iostream>
#include <locale.h>

using namespace std;

// O IMC é uma medida geral e pode não levar em consideração fatores como composição corporal, massa muscular ou distribuição de gordura

int main() {
    // Configura a localidade para português
    setlocale(LC_ALL, "portuguese");

    float peso, altura, imc;

    // Usando um loop for para calcular o IMC de apenas uma pessoa
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
