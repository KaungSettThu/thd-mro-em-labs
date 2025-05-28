import os
import time
import numpy as np
from sense_hat import SenseHat

sense = SenseHat()

LABEL = "move_none" # change to "move_shake", "move_twist" or "move_none" for otther classes

# set sampling parameters

SAMPLES = 50
FREQ_HZ = 50
DELAY = 1.0 / FREQ_HZ

# create save directory

save_dir = f"./motion_data/{LABEL}"
os.makedirs(save_dir, exist_ok=True)

# take sample

print(f"Recording samples for label: {LABEL}")
try:
    while True:
        input("Press Enter to record 1 second")

        data = []

        for _ in range(SAMPLES):

            # take accelerometer and gyroscopic data

            acc = sense.get_accelerometer_raw()
            gyro = sense.get_gyroscope_raw()

            sample = [
                acc['x'], acc['y'], acc['z'],
                gyro['x'], gyro['y'], gyro['z']
            ]

            # append the sample to the data array

            data.append(sample)

            time.sleep(DELAY)

        timestamp = int(time.time())

        # save the sammple as a file with the time stamp

        np.save(f"{save_dir}/{LABEL}_{timestamp}.npy", np.array(data))

        print(f"Saved {LABEL}_{timestamp}.npy")

except KeyboardInterrupt:
    print("Recording stopped...")