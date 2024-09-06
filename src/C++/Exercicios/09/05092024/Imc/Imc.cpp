#include <iostream>
#include <locale.h>

using namespace std;

int main() {
	// Configura a localidade para português
	setlocale(LC_ALL, "pt_BR.UTF-8");

	float peso, altura, imc;

	cout << "Digite seu peso: ";
	cin >> peso;

	cout << "Digite sua altura: ";
	cin >> altura;

	imc = peso / (altura * altura);

	if (imc <= 18.5) {
		cout << "Magreza";

	}
	else if ((imc >= 18.6) && (imc < 24.9) ) {
		cout << "Peso normal";
	}
	else if ( (imc >= 25) && (imc < 29.9)) {
		cout << "Obesidade de grau I";

	}else if ((imc >= 35) && (imc < 39.9)) {
		cout << "Obesidade de grau II";

	}
	else {
		cout << "Obesidade de grau III";
	}

	return 0;
}