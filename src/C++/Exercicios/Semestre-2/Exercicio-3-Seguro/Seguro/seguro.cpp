#include <iostream>
#include <locale.h>

using namespace std;

int main()
{
	int idade;
	char grupo;

	// Configura a localidade para portugu�s
	setlocale(LC_ALL, "portuguese");

	cout << "Informe sua idade" << endl;;
	cin >> idade;

	cout << "Informe o grupo" << endl;
	cin >> grupo;

	
	if ((idade >= 18) && (idade <= 70)) {
		
		switch (grupo) {
		case 'b':
			
			if ((idade >= 18) && (idade <= 24)) {
				cout << "C�digo � 7";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "C�digo � 4";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "C�digo � 1";
			}
			break;

		case 'm':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "C�digo � 8";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "C�digo � 5";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "C�digo � 2";
			}
			break;
			break;

		case 'a':
			if ((idade >= 18) && (idade <= 24)) {
				cout << "C�digo � 9";
			}
			else  if ((idade >= 25) && (idade <= 40)) {
				cout << "C�digo � 6";
			}
			else if ((idade >= 41) && (idade <= 70)) {
				cout << "C�digo � 3";
			}
			break;
			break;

		default:
			cout << "Grupo n�o reconhecido";
			break;
		}

	}
	else {;
		cout << "Voc� n�o pode adquirir um sseguro";
	}

	return 0;
}