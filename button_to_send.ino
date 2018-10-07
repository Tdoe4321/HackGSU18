//pins used for components
const int buzzer = 4;   // Arduino port pin PD4
int crashButton = A1;
int resetButton =A2;
int LED1 = 3;
int LED2 = 9;
boolean isOn = true;
boolean didCrash = false;
unsigned long switchTime = 0;
    
void setup(){
    pinMode(buzzer, OUTPUT); // set pin for buzzer output
    pinMode(crashButton, INPUT);
    pinMode(resetButton, INPUT); 

    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);

    Serial.begin(9600);
}

void loop(){
    //if(analogRead(A0) >= 20){
    //   digitalWrite(LED2, HIGH);
    //}
    //else{
    //   digitalWrite(LED2, LOW);
    //}
    if(/*digitalRead(crashButton)*/ analogRead(A0) > 20) {
	didCrash = true;
	digitalWrite(LED1, HIGH);
	digitalWrite(LED2, HIGH);
	switchTime = millis();
	Serial.print(1);
	Serial.println();
    }
    else{
	}
    if(digitalRead(resetButton)) {
	Serial.print(0);
	Serial.println();
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
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
