// C++ code
//
void setup()
{
 pinMode(13, OUTPUT);
   pinMode(12, OUTPUT);
   pinMode(11, OUTPUT);
   pinMode(9, OUTPUT);
   pinMode(8, OUTPUT);
}
void loop()
{
  digitalWrite(13 , HIGH);
  digitalWrite(12 , LOW);
  digitalWrite(11 , LOW);
  // Pedrestre
  digitalWrite(9 , LOW);
  digitalWrite(8 , HIGH);
  delay(1000);
  digitalWrite(13 , LOW);
  digitalWrite(12 , HIGH);
  digitalWrite(11 , LOW);
  // Pedrestre
  digitalWrite(9 , HIGH);
  digitalWrite(8 , LOW);
  delay(500);
  digitalWrite(13 , LOW);
  digitalWrite(12 , LOW);
  digitalWrite(11 , HIGH);
  // Pedrestre
  digitalWrite(9 , HIGH);
  digitalWrite(8 , LOW);
  delay(1500);
}