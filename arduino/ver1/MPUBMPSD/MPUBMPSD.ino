//==========================
//   Rocket Data Collector:
//==========================

///////////////////////////////////
// Gilicze Kristóf 2016/08/17   //
// Összevont verzió 1.0        //
///////////////////////////////


#include <EEPROM.h>				//EEPROM a mérés számának tárolása
#include <Wire.h>				// I2C protokoll könyvtár importálása a szenzorokkal való kommunikációhoz.
#include "mpu6050_defines.h" 

short int meres_sorszam = 0;	

//BMP180
#include <Adafruit_BMP085.h> 
Adafruit_BMP085 bmp;
float kezdeti_nyomas;
float alt;




float x_tengely_acc;



void setup()
{
Wire.begin();			//I2C indítása
Serial.begin(115200);	//Serial kapcsolat indítása > USB hibakereséshez
Serial1.begin(115200);	//Serial kapcsolat indítása a ESP8266 modul felé

//==========================================================
//  TCP/IP kommunikáció létrehozása kapcsolodás a Routerhez
//==========================================================
Serial1.println("AT+CWLAP");
serial1toUSB();
Serial1.println('AT+CWJAP="hun220","123456789"');
serial1toUSB();



//======================================
//  BMP180 startup script
//======================================
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






//==========================================================
//  MPU6050 inicializálása
//==========================================================

  // Set up the interrupt pin, its set as active high, push-pull
  pinMode(intPin, INPUT);
  digitalWrite(intPin, LOW);
  uint8_t c = readByte(MPU6050_ADDRESS, WHO_AM_I_MPU6050);  // Read WHO_AM_I register for MPU-6050

  delay(1000);

  if(c == 0x68) // WHO_AM_I should always be 0x68
  {
    Serial.println("MPU6050 elérheto...");

    MPU6050SelfTest(SelfTest); // Start by performing self test and reporting values
    Serial.print("x-axis self test: acceleration trim within : "); Serial.print(SelfTest[0],1); Serial.println("% of factory value");
    Serial.print("y-axis self test: acceleration trim within : "); Serial.print(SelfTest[1],1); Serial.println("% of factory value");
    Serial.print("z-axis self test: acceleration trim within : "); Serial.print(SelfTest[2],1); Serial.println("% of factory value");
    Serial.print("x-axis self test: gyration trim within : "); Serial.print(SelfTest[3],1); Serial.println("% of factory value");
    Serial.print("y-axis self test: gyration trim within : "); Serial.print(SelfTest[4],1); Serial.println("% of factory value");
    Serial.print("z-axis self test: gyration trim within : "); Serial.print(SelfTest[5],1); Serial.println("% of factory value");

    if(SelfTest[0] < 1.0f && SelfTest[1] < 1.0f && SelfTest[2] < 1.0f && SelfTest[3] < 1.0f && SelfTest[4] < 1.0f && SelfTest[5] < 1.0f) {

    delay(1000);

    calibrateMPU6050(gyroBias, accelBias); // Calibrate gyro and accelerometers, load biases in bias registers
    initMPU6050(); Serial.println("MPU6050 sikeresen inicalizalba...."); //Sikeres kapcsolodás, felhasználó tájékoztatása

   }
   else
   {
    Serial.print("Nem sikerult a kapcsolat a MPU6050-hoz: 0x");
    Serial.println(c, HEX);
    while(1) ; // Loop forever if communication doesn't happen
   }

  }
}




void loop()
{
  // If data ready bit set, all data registers have new data
  if(readByte(MPU6050_ADDRESS, INT_STATUS) & 0x01) {  // check if data ready interrupt

    readAccelData(accelCount);  // Gyorsulásadatok olvasása
    getAres();

    // Now we'll calculate the accleration value into actual g's
    ax = (float)accelCount[0]*aRes - accelBias[0];  // get actual g value, this depends on scale being set
    ay = (float)accelCount[1]*aRes - accelBias[1];
    az = (float)accelCount[2]*aRes - accelBias[2];
	
/* GYROSCOPE AND TEMP CURRENTLY DISABLED
    readGyroData(gyroCount);  // Read the x/y/z adc values
    getGres();

   // Calculate the gyro value into actual degrees per second
    gx = (float)gyroCount[0]*gRes - gyroBias[0];  // get actual gyro value, this depends on scale being set
    gy = (float)gyroCount[1]*gRes - gyroBias[1];
    gz = (float)gyroCount[2]*gRes - gyroBias[2];

    tempCount = readTempData();  // Read the x/y/z adc values
    temperature = ((float) tempCount) / 340. + 36.53; // Temperature in degrees Centigrade
    */
   }

	uint32_t deltat = millis() - count;
    if(deltat > 2) {

    // Print acceleration values in milligs!
	//Serial.print(1000*ax); Serial.print(";");
	// Serial.print(1000*ay); Serial.print(";");
    meres_sorszam++;
    1000*az = x_tengely_acc;
    bmp.readAltitude(kezdeti_nyomas-10) = alt; //magasság kiolvasása
    
    Serial.print(meres_sorszam);
    Serial. print(":    ");
    Serial.print(x_tengely_acc);
    Serial.print("  -   ");
    Serial.print(alt);
    Serial.println();

    // Print gyro values in degree/sec
    // Serial.print("X-gyro rate: "); Serial.print(gx, 1); Serial.print(" degrees/sec ");
   //  Serial.print("Y-gyro rate: "); Serial.print(gy, 1); Serial.print(" degrees/sec ");
   //  Serial.print("Z-gyro rate: "); Serial.print(gz, 1); Serial.println(" degrees/sec");

   // Print temperature in degrees Centigrade
   // Serial.print(temperature, 2); // Print T values to tenths of s degree C
   // Serial.println("");
    
    count = millis(); //Stopper tárolása
    }

}

