#include <iostream>
#include <locale.h>

using namespace std;

int main() {
    float salario_minimo, horas_trabalhadas, horas_extras;
    int dependentes;

    setlocale(LC_ALL, "portuguese");

    cout << "Informe o valor do salário mínimo: R$ ";
    cin >> salario_minimo;
    cout << "Informe o número de horas trabalhadas: ";
    cin >> horas_trabalhadas;
    cout << "Informe o número de dependentes: ";
    cin >> dependentes;
    cout << "Informe a quantidade de horas extras trabalhadas: ";
    cin >> horas_extras;

    float valor_hora_trabalhada = salario_minimo / 5;

    float salario_mes = horas_trabalhadas * valor_hora_trabalhada;

    float valor_dependentes = dependentes * 32.00;

    float valor_hora_extra = valor_hora_trabalhada * 1.5;
    float valor_horas_extras = horas_extras * valor_hora_extra;


    float salario_bruto = salario_mes + valor_dependentes + valor_horas_extras;

    float irrf;
    if (salario_bruto < 200) {
        irrf = 0;
    }
    else if (salario_bruto <= 500) {
        irrf = salario_bruto * 0.10;
    }
    else {
        irrf = salario_bruto * 0.20;
    }

    float salario_liquido = salario_bruto - irrf;

    float gratificacao;
    if (salario_liquido <= 350) {
        gratificacao = 100;
    }
    else {
        gratificacao = 50;
    }

    float salario_final = salario_liquido + gratificacao;

    cout << "\nSalário bruto: R$ " << salario_bruto << endl;
    cout << "IRRF: R$ " << irrf << endl;
    cout << "Salário líquido: R$ " << salario_liquido << endl;
    cout << "Gratificação: R$ " << gratificacao << endl;
    cout << "Salário final a receber: R$ " << salario_final << endl;

    return 0;
}
