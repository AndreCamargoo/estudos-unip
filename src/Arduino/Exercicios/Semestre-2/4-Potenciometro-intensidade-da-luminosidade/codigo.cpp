int POT = A1;
int LED = 9;
int valor = 0;
void setup() {
 Serial.begin(9600);
  pinMode(LED, OUTPUT);
}
void loop() {
 valor = analogRead(POT);
 if(valor > 0) {
 // Acende o led com intensidade proporcional
 // ao valor obtido
 analogWrite(LED, (valor/4));
 // Exibe no Serial Monitor o valor obtido
 // do potenciômetro
 Serial.println(valor);
 }
}