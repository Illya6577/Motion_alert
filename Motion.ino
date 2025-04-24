int pirPin = 7;
int ledPin = 13;

int val = 0;

void setup()
{
Serial.begin(9600);
pinMode(pirPin, INPUT);
pinMode(ledPin, OUTPUT);
pinMode(3, OUTPUT);
}

void loop () {
val = digitalRead(pirPin);
if (val == HIGH)
    {
    	 digitalWrite(ledPin, LOW);
    	 Serial.println("Motion!");
  		 digitalWrite(3,HIGH);
    }
else
    {
      	digitalWrite(ledPin, LOW);
      	Serial.println("No motion");
  		digitalWrite(3,LOW);
    }
delay(100);
}