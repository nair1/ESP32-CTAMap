from machine import Pin
import time

data = Pin(23, Pin.OUT) # SER (serial data input)
latch = Pin(22, Pin.OUT) # RCLK (storage register clock input)
clock = Pin(21, Pin.OUT) # SRCLK (shift register clock input)
srclr = Pin(19, Pin.OUT) # SRCLR (clear register)

def shift_bit(value):
    data.value(value)
    clock.value(1)
    clock.value(0)

def update_register():
    latch.value(1)
    latch.value(0)

def clear_register():
    srclr.value(0)
    srclr.value(1)

def shift_and_update_whole_number(value):
    for _ in range(0, 8):
        bit = value & 1
        shift_bit(bit)
        value >>= 1
        
        update_register()

clear_register()

while True:
    numbers = [0, 128, 32, 160, 8, 136, 40, 168, 2, 130, 34, 162, 10, 138, 42, 170]
    
    for number in numbers:
        shift_and_update_whole_number(number)
        time.sleep(0.5)