#include <iostream>
#include <locale.h>

using namespace std;

int main(){

	setlocale(LC_ALL, "portuguese");

	float horasExtras, horasFalta, premio;

	cout << "Digite as horas extras" << endl;
	cin >> horasExtras;

	cout << "Digite as horas faltas" << endl;
	cin >> horasFalta;

	cout << "Suas horas extras foram de: " << horasExtras*60 << " minutos" << endl;
	cout << "Suas horas faltas foram de: " << horasFalta * 60 << " minutos" << endl;

	premio = (horasExtras * 60) - (2 / 3 * (horasFalta * 60));

	if (premio > 2400) {
		cout << "Seu premio será de R$ 500";
	}
	else if ( (premio >= 1800) && (premio < 2400) ) {
		cout << "Seu premio será de R$ 400";
	}
	else if ((premio >= 1200) && (premio < 1800)) {
		cout << "Seu premio será de R$ 300";
	}
	else if ((premio >= 600) && (premio < 1200)) {
		cout << "Seu premio será de R$ 200";
	}
	else {
		cout << "Seu premio será de R$ 100";
	}

}