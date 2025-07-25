from sense_hat import SenseHat
import time

sense = SenseHat()

while True:

    # Get environment readings from the sense hat
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    # Display the results
    print(f"Temp: {temp:.1f}C; Humidity: {humidity:.1f}%; Pressure: {pressure:.1f}hPa")

    # Set delay
    time.sleep(2)

