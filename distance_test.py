"""Example for distance sensor"""

from signal import pause
import time
from buildhat import DistanceSensor, Motor

motor = Motor('A')
dist = DistanceSensor('D', threshold_distance=70)

motor.set_default_speed(-25)
print("Start motor")
motor.start()

def handle_in(distance):
    """Within range

    :param distance: Distance
    """
    motor.stop()
    print("in range", distance)


def handle_out(distance):
    """Out of range

    :param distance: Distance
    """
    motor.start()
    print("out of range", distance)


dist.when_in_range = handle_in
dist.when_out_of_range = handle_out
try:
    pause()  # This will keep the program running
except KeyboardInterrupt:
    print("Stopping motor and exiting...")
    motor.stop()  # Stop the motor when exiting
