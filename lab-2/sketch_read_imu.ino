# include "Arduino_BMI270_BMM150.h"

void setup() {
    Serial.begin(9600);

    while (!Serial);
    if (!IMU.begin()) {
        Serial.println("IMU initilization failed!");
        while (1);
    }
}

void loop() {
    // Declare acceleration variables
    float x, y, z;

    // Read and display sensor data
    if(IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);
        Serial.,print("Acceleration:");
        Serial.print(" X = "); Serial.print(x);
        Serial.print(" Y = "); Serial.print(y);
        Serial.print(" Z = "); Serial.print(z);
        Serial.println();
    }

    // Delay of 500 ms
    delay(500);
}