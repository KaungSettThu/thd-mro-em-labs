#include <Arduino_HS300x.h>

void setup() {
    Serial.begin(9600);
    
    while (!Serial);
    if (!IMU.begin()) {
        Serial.println("HS300 initilization failed!");
        while (1);
    }
}

void loop() {
    // take temperature reading
    float temp = HS300x.readTemperature();
    
    // take humidity reading
    float humidity = HS300x.readHumidity();

    // display results
    Serial.print("Temp: "); Serial.print(temp); Serial.print("C  ");
    Serial.print("Humidity: "); Serial.print(humidity); Serial.print("%");
    Serial.println();

    // delay for 2 sec
    delay(2000)
}