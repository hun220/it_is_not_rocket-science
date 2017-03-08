


#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;
float kezdeti_nyomas;



void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
	Serial.println("Nem elerheto BMP180 Altimeter, ellenorizd a kabeleket!");
	while (1) {}
  }
    Serial.print("LEGNYOMAS MINTAVETEL MAGASSAG MERESHEZ...");
    Serial.print("Kezdeti nyomas = ");
    kezdeti_nyomas = bmp.readPressure();
    Serial.print(kezdeti_nyomas);
    Serial.println(" Pa");
}
  
void loop() {
    Serial.print("Jelenlegi magassag = ");
    Serial.print(bmp.readAltitude(kezdeti_nyomas-10));
    Serial.println(" meter");
    
    Serial.println();
    delay(500);
}
