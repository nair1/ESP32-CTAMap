from machine import Pin
import time

onboard_led = Pin(2, Pin.OUT)

blinks_per_sec = 4
blink_time = 1.0 / blinks_per_sec

while (True):
    onboard_led.on()
    time.sleep(blink_time)
    onboard_led.off()
    time.sleep(blink_time)
