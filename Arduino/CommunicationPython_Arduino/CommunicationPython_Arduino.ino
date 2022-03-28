int mesure;
void setup() {
 Serial.begin(9600);

}

void loop() {
  while(!Serial.available())continue;
  if(Serial.read()=='*'){
    mesure=analogRead(0);
    Serial.print(mesure);
  }

}
