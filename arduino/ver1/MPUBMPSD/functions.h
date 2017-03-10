void serial1toUSB()
{
	string buffer = "";
	while (!buffer)
		{
			if (Serial1.available())
				{
					buffer = Serial1.read();
					Serial.write();
					delay(10);
				}
		}
}