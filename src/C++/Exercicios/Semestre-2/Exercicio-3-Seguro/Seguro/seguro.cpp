#include <iostream>
#include <locale.h>

using namespace std;

int main()
{
	int idade;
	char grupo;

	setlocale(LC_ALL, "portuguese");

	cout << "Informe sua idade" << endl;
	cin >> idade;

	cout << "Informe o grupo" << endl;
	cin >> grupo;

	
	if ((idade >= 18) && (idade <= 70)) {
		
		switch (grupo) {
		case 'b':
			
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 7" << endl;
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 4"<< endl;
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 1"<< endl;
			}
			break;

		case 'm':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 8" << endl;
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 5" << endl;
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 2" << endl;
			}
			break;
			break;

		case 'a':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "Código é 9" << endl;
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "Código é 6" << endl;
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "Código é 3" << endl;
			}
			break;
			break;

		default:
			cout << "Grupo não reconhecido";
			break;
		}

	}
	else {;
		cout << "Você não pode adquirir um seguro";
	}

	return 0;
}