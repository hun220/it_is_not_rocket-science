
//==========================
//   Rocket Data Collector:
//==========================

///////////////////////////////////
// Gilicze Kristóf 2016/08/17   //
// Összevont verzió 1.0        //
///////////////////////////////

#include <Wire.h>
#include "functions.h"
#include "mpu6050_defines.h" 

short int meres_sorszam = 0;	

//BMP180
#include <Adafruit_BMP085.h> 
Adafruit_BMP085 bmp;
float kezdeti_nyomas;
float alt;
float x_tengely_acc;
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

void setup()
{
Wire.begin();			//I2C indítása
Serial.begin(115200);	//Serial kapcsolat indítása > USB hibakereséshez
display.begin(SSD1306_SWITCHCAPVCC, 0x3C); //Képernyő indítása 0x3C címen (128x32)
delay(800);


  //Buffer törlése, Start felirat megjelenítése:
  display.clearDisplay();
  display.setRotation(2);
  display.setTextSize(1.3);
  display.setTextColor(WHITE);
  display.setCursor(20,10);
  display.println("SCREEN STARTED!");
	display.display();
  delay(900);

//==========================================================
//  TCP/IP kommunikáció létrehozása kapcsolodás a Routerhez
//==========================================================


  //OLED frissítése a hálozat állapotáról
  display.clearDisplay();
  display.setCursor(20,10);
  display.println("Network Online!");
  display.display();
  delay(900);
  

//=====================================================================================================================================
//  BMP180 szenzor inicializálása, késöbb szükségünk lesz a földön készített légnyomás adatokra, a barometrikus magasságméréshez
//=====================================================================================================================================
  if (!bmp.begin())
    { // HIBAÜZENETEK:

      Serial.println("Nem elerheto BMP180 Altimeter, ellenorizd a kabeleket!");

      //OLED frissítése a hálozat állapotáról
      display.clearDisplay();
      display.setCursor(20,10);
      display.println("ERROR BMP180");
      display.display();

    while (1) {}

    }

  else
    {

      Serial.print("LEGNYOMAS MINTAVETEL MAGASSAG MERESHEZ...");
      Serial.print("Kezdeti nyomas = ");
      kezdeti_nyomas = bmp.readPressure();

      //Képernyő és Serial Frissitése a légnyomás adatokkal.
      display.clearDisplay();
      display.setCursor(10,5);
      display.println("Kezdeti nyomas: ");
      display.println(kezdeti_nyomas);
      display.display();
      Serial.print(kezdeti_nyomas);
      Serial.println(" Pa");

    }


//==============================================================================================
//  MPU6050 inicializálása, a szükséges I2C címek a "mpu6050_defines.h" file-ban vannak mapelve
//==============================================================================================

  //Interupt pin, magas aktív beállításban, a MPU6050 megszakítja az egyéb folyamatokat amikor adat elérhető.
  pinMode(intPin, INPUT); //Interupt pin inicializálása mint bemenet
  digitalWrite(intPin, LOW);
  uint8_t c = readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050);  //Kapcsolat ellenörzése, a I2C cím- segítségével.

  delay(500);

  if(c == 0x68) // WHO_AM_I MPU6050-es IMU esetében általában 0x68
  {
    //Képernyők frissitése arról hogy az MPU6050 elérhető
    Serial.println("MPU6050 elérheto...");
    display.clearDisplay();
    display.setCursor(20,10);
  	display.print("MPU-6050 UP");
  	display.display();
    delay(900);
  
    MPU6050SelfTest(SelfTest); // Indítás egy test futtatásával
    Serial.print("x-axis self test: acceleration trim within : "); Serial.print(SelfTest[0],1); Serial.println("% of factory value");
    Serial.print("y-axis self test: acceleration trim within : "); Serial.print(SelfTest[1],1); Serial.println("% of factory value");
    Serial.print("z-axis self test: acceleration trim within : "); Serial.print(SelfTest[2],1); Serial.println("% of factory value");
    Serial.print("x-axis self test: gyration trim within : "); Serial.print(SelfTest[3],1); Serial.println("% of factory value");
    Serial.print("y-axis self test: gyration trim within : "); Serial.print(SelfTest[4],1); Serial.println("% of factory value");
    Serial.print("z-axis self test: gyration trim within : "); Serial.print(SelfTest[5],1); Serial.println("% of factory value");

    if(SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f && SelfTest[5] < 1.0f) {
    
    delay(1000);

    
    calibrateMPU6050(gyroBias, accelBias);                  //Szenzormodul kalibrálása
    initMPU6050();                                          //Sikeres kapcsolodás
    Serial.println("MPU6050 sikeresen inicalizalva....");   //felhasználó tájékoztatása

   }
   else
   {
    //MPU6050 nem elérhető, U tájékoztatása.
    Serial.print("Nem sikerult a kapcsolat a MPU6050-hoz: 0x");
    Serial.println(c, HEX);
    while(1) ;
   }

  }
}




void loop()
{

  if(readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01)//Elleneröziük hogy van-e elérhető adat
    { 
    

    //Gyorsulás

    readAccelData(accelCount);  // Gyorsulásadatok olvasása
    getAres();

    //G- érték kalkulálása
    ax = (float)accelCount[0]*aRes - accelBias[0];  
    ay = (float)accelCount[1]*aRes - accelBias[1];
    az = (float)accelCount[2]*aRes - accelBias[2];


    //Giroszkóp

    readGyroData(gyroCount);  // Read the x/y/z adc values
    getGres();

   //Gyroscope adatok kalkulálása Fok/másodperc-be.
    gx = (float)gyroCount[0]*gRes - gyroBias[0]; 
    gy = (float)gyroCount[1]*gRes - gyroBias[1];
    gz = (float)gyroCount[2]*gRes - gyroBias[2];

   }

	  uint32_t deltat = millis() - count;
    if(deltat > 2) {

    //Gyorsulás adatok átváltása MILIG-be
	  //Serial.print(1000*ax); Serial.print(";");
	  // Serial.print(1000*ay); Serial.print(";");
    meres_sorszam++;
    alt = bmp.readAltitude(kezdeti_nyomas); //magasság kiolvasása
    
    Serial.print(meres_sorszam);
    Serial. print(":    ");
    Serial.print(ax);
    Serial.print(";");
    Serial.print(alt);
    Serial.println();
    
	display.setTextSize(2);
	display.clearDisplay();
	display.setCursor(0,0);
	display.print(x_tengely_acc);display.setTextSize(1);display.println(" G");
  display.setCursor(0,16);
  display.setTextSize(2);
  display.print(alt);display.setTextSize(1);display.println(" m");
	display.display();

    count = millis(); //Stopper tárolása
    }

}

