//pins used for components
const int buzzer = 4;   // Arduino port pin PD4
const int crashButton = 5;
const int resetButton = 6;
boolean isOn = true;
boolean didCrash = false;
unsigned long switchTime = 0;
    
void setup(){
    pinMode(buzzer, OUTPUT); // set pin for buzzer output
    pinMode(crashButton, INPUT);
}

void loop(){
    
    if(digitalRead(crashButton) == HIGH) didCrash = true;
    if(digitalRead(resetButton) == HIGH) didCrash = false;

    if(millis() - switchTime > 3000) {
        if(isOn) isOn = false;
		else isOn = true;
        switchTime = millis();
    }
    
    if (isOn){
	digitalWrite(buzzer, LOW);
        //digitalWrite(buzzer, HIGH);
    }
    else
        digitalWrite(buzzer, LOW);
}
