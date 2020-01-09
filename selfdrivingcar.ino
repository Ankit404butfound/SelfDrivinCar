void setup() {
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  if (Serial.available()) {
  int info = Serial.read();
    if (info == 'r'){           //When red light
      digitalWrite(10,LOW);
      digitalWrite(11,LOW);
    }
    if (info == 'y'){           //When red light
      analogWrite(10,200);
      analogWrite(11,200);
      analogWrite(10,100);
      analogWrite(11,100);
      analogWrite(10,50);
      analogWrite(11,50);
    }
    if (info == 'y'){
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
    }
}
