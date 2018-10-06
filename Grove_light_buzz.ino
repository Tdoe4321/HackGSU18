//pins used for components
const int buzzer = 4;   // Arduino port pin PD4
boolean isOn = true;
unsigned long switchTime = 0;
    
void setup(){
    pinMode(buzzer, OUTPUT); // set pin for buzzer output
}

void loop(){
    
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
