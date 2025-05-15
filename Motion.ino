int pirPin = 7;

int val = 0;

void setup()
{
Serial.begin(9600);
pinMode(pirPin, INPUT);
}

void loop () {
val = digitalRead(pirPin);
if (val == HIGH)
    {
    	 Serial.println("Motion!");
    }
else
    {
      	Serial.println("No motion");
    }
delay(100);
}
