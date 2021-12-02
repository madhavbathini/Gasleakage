#include<SoftwareSerial.h> // liBRARY FUNCTIONS TO ALLOW SERIAL COMMUNICATION

#include<LiquidCrystal.h> // ALLOW COMMUNICATION WITH LCD

#define gas_sensor A0
#define Buzzer A1

int gas_value;

LiquidCrystal lcd (2,3,4,5,6,7);  //LCD CONNECTIONS
SoftwareSerial mySerial(12, 13);  //GSM CONNECTIONS

void setup() {

Serial.begin(9600); // STARTS SERIAL COMMUNICTAION

mySerial.begin (9600);  //

lcd.begin(16,2);   // INITIALOZE LCD SCREEEN
pinMode (gas_sensor, INPUT); // TO CONFIGURE SPECIFIC PIN FOR INPUT OR OUTPUT

pinMode(Buzzer,OUTPUT);   //BUZZER PIN FOR OUTPUT

lcd.setCursor(0,0); // POSITION TO DISPLAY

lcd.print("   Gas Leakage");

lcd.setCursor (0,1);  // POSITION

lcd. print ("    detection");
delay (2000); // STOPS AFTER 2 SECOND
lcd.clear();
}

void loop() {

gas_value=analogRead(A0); // READS THE VALUE FROM GAS VALUE
Serial.println(gas_value);   // PRINT GAS VALUE ON LCD
lcd.print ("Gas Scan is ON"); // PRINT ON LCD
lcd.setCursor(0,1); 
lcd.print("Gas Level: ");
lcd.print(gas_value);
delay(1000);

if(gas_value>100)
{
  sendMessage(); // USING FUNCTION TO SEND MESSAGE
  Serial.print("Gas detect alarm");
lcd.clear();
lcd.setCursor(0,0);
lcd.print("Gas Level Exceed");
  Serial.print("Buzzer ON");
  digitalWrite(Buzzer,1);
  delay(2000);
  digitalWrite(Buzzer,0);
  delay(1000);
 digitalWrite(Buzzer,1);
  delay(2000);
  digitalWrite(Buzzer,0);
  lcd.setCursor(0,1);
  lcd.print("SMS Sent");
delay(1000);
}
else
{
  Serial.println("Buzzer OFF");
  delay(1000);
}
}
  void sendMessage()
  {
  Serial.println(" gas leakage going on");
  mySerial.println("AT+CMGF=1");    //To send SMS in Text Mode TO SUPPORT GSM(COMMAND)
  delay(1000);
  mySerial.println("AT+CMGS=\"+919392781953\"\r"); // change to the phone number you using (CMGS=SEND MESSAGE)
  delay(1000);
  mySerial.println("Gas Leaking!");//the content of the message
  delay(200);
  mySerial.println((char)26);//the stopping character
  delay(1000);
}