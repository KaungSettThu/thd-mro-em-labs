import os
import time
from datetime import datetime
from picamera2 import Picamera2

# pick the gesture and folder

gesture = " thumbs_up " # or " no_thumbs_up "
save_dir = f"./ gesture_data /{ gesture }"
os . makedirs ( save_dir , exist_ok = True )

# configure and start the camera

picam2 = Picamera2 ()

# 640 480 still capture

still_cfg = picam2 . create_still_configuration (
    main ={" format ": " RGB888 ", " size ": (640 , 480) }
)
