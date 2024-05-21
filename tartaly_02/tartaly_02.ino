#include <LiquidCrystal.h>

#include <Wire.h>




int thrs = 20;
int pinOut = 10;
int ledPin = 10;
char command;

int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


void setup() {
Serial.begin(9600);
pinMode(10, OUTPUT);

}

void loop()
 {
  lcd.setCursor(0, 0);

  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 

  Serial.println(Tc);

  lcd.print("Temp: ");
  lcd.print(Tc);   
  lcd.print(" C");

  if (Serial.available() > 0) {
    int command = Serial.parseInt();
    thrs = command;
  }

  if (Tc > thrs){
    digitalWrite(pinOut,  HIGH);
  }
  else {
    digitalWrite(pinOut, LOW);
  }

  
 
  delay(500);
  lcd.clear();
  
}