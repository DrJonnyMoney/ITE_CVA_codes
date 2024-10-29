from gpiozero import LED
import time
from tqdm import tqdm

led = LED(23)
led.off()

start_time = time.time()
duration = 10

with tqdm(total=duration, dynamic_ncols=True) as pbar:
    while time.time()-start_time < duration:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
        elapsed_time = time.time() - start_time
        pbar.update(min(elapsed_time - pbar.n, duration - pbar.n))

print("Program Ended.")
led.off()
