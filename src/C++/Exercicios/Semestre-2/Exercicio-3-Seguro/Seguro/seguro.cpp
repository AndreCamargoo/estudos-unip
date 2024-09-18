#include <iostream>
#include <locale.h>

using namespace std;

int main()
{
	int idade;
	char grupo;

	// Configura a localidade para português
	setlocale(LC_ALL, "portuguese");

	cout << "Informe sua idade" << endl;;
	cin >> idade;

	cout << "Informe o grupo" << endl;
	cin >> grupo;

	
	if ((idade >= 18) && (idade <= 70)) {
		
		switch (grupo) {
		case 'b':
			
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 7";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 4";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 1";
			}
			break;

		case 'm':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 8";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 5";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 2";
			}
			break;
			break;

		case 'a':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 9";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 6";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 3";
			}
			break;
			break;

		default:
			cout << "Grupo não reconhecido";
			break;
		}

	}
	else {;
		cout << "Você não pode adquirir um sseguro";
	}

	return 0;
}