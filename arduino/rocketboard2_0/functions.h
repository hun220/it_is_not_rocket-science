

  void writeByte(uint8_t address, uint8_t subAddress, uint8_t data)
{
  Wire.beginTransmission(address);  // Initialize the Tx buffer
  Wire.write(subAddress);           // Put slave register address in Tx buffer
  Wire.write(data);                 // Put data in Tx buffer
  Wire.endTransmission();           // Send the Tx buffer
}

  uint8_t readByte(uint8_t address, uint8_t subAddress)
{
  uint8_t data; // `data` will store the register data
  Wire.beginTransmission(address);         // Initialize the Tx buffer
  Wire.write(subAddress);                  // Put slave register address in Tx buffer
  Wire.endTransmission(false);             // Send the Tx buffer, but send a restart to keep connection alive
  Wire.requestFrom(address, (uint8_t) 1);  // Read one byte from slave register address
  data = Wire.read();                      // Fill Rx buffer with result
  return data;                             // Return data read from slave register
}

  void readBytes(uint8_t address, uint8_t subAddress, uint8_t count, uint8_t * dest)
{
  Wire.beginTransmission(address);   // Initialize the Tx buffer
  Wire.write(subAddress);            // Put slave register address in Tx buffer
  Wire.endTransmission(false);       // Send the Tx buffer, but send a restart to keep connection alive
  uint8_t i = 0;
        Wire.requestFrom(address, count);  // Read bytes from slave register address
  while (Wire.available()) {
        dest[i++] = Wire.read(); }         // Put read results in the Rx buffer
}



alt_buffer = {0,0,0,0,0,0,0,0,0,0};

  bool ejtoernyo_check(float curr_alt)
  {
    if ejtoernyo_nyitva = false{
    int ernyo = 0;	
    //Magasság buffer frissítése
   for(int i = 0; i < 9; i++)
    { 
      if(alt_buffer[i] > alt_buffer[i+1])
        {
        ernyo++;	
        }	
      alt_buffer[i] = alt_buffer[i+1];
    }
  alt_buffer[9] = curr_alt;

  if(ernyo > 7)
    {
    //szervo_nyit
    GlobaL_ejtoernyo_nyitva = true
    return true;
    }
    else
    {
    return false;
    }
    }

}
