#include <iostream>
#include <locale.h>

using namespace std;

int main() {
	// Configura a localidade para portugu�s
	setlocale(LC_ALL, "pt_BR.UTF-8");

	float n1, n2, n3, mp;

	cout << "Digite sua primeira nota: ";
	cin >> n1;

	cout << "Digite sua segunda nota: ";
	cin >> n2;

	cout << "Digite sua terceira nota: ";
	cin >> n3;

	mp = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5);


	// Verifica��o da nota e exibi��o de mensagens
	if ((mp >= 8) && (mp <= 10)) {
		cout << "Sua nota foi " << mp << ". �timo!" << endl;
	}
	else if ( (mp >= 7) && (mp < 8) ) {
		cout << "Sua nota foi " << mp << ". Na m�dia!" << endl;
	}
	else if ( (mp >= 6) && (mp < 7) ) {
		cout << "Sua nota foi " << mp << ". Preocupante, mais passou!" << endl;
	}
	else if ( (mp >= 5) && (mp < 6) ) {
		cout << "Sua nota foi " << mp << ". Exame!" << endl;
	}
	else {
		cout << "Sua nota foi " << mp << ". Reprovou!" << endl;
	}

	return 0;
}