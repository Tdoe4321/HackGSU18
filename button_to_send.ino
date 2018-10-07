//pins used for components
const int buzzer = 4;   // Arduino port pin PD4
int crashButton = A1;
int resetButton =A2;
boolean isOn = true;
boolean didCrash = false;
unsigned long switchTime = 0;
    
void setup(){
    pinMode(buzzer, OUTPUT); // set pin for buzzer output
    pinMode(crashButton, INPUT);
    pinMode(resetButton, INPUT);

    Serial.begin(9600);
}

void loop(){
    
    if(digitalRead(crashButton)) {
	didCrash = true;
	switchTime = millis();
	Serial.print(1);
	Serial.println();
    }
    else{
	}
    if(digitalRead(resetButton)) {
	Serial.print(0);
	Serial.println();
	didCrash = false;
    }

    if(millis() - switchTime > 3000) {
        if(isOn) isOn = false;
		else isOn = true;
        switchTime = millis();
    }
    
    if (isOn && didCrash){
	//digitalWrite(buzzer, LOW);
        digitalWrite(buzzer, HIGH);
    }
    else
        digitalWrite(buzzer, LOW);
}
