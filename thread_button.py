from gpiozero import LED, Button
from time import sleep
import threading

def listen_for_keypress():
    print("Press Me Again!")
    button.wait_for_press()
        
button = Button(2)
led = LED(23)

print("Press Me!")
button.wait_for_press()
sleep(1)

keypress_thread = threading.Thread(target=listen_for_keypress)
keypress_thread.start()

while keypress_thread.is_alive():
    led.on()
    sleep(3)

print("Powering Down!")
led.off()