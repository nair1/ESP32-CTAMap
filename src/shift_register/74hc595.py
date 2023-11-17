from machine import Pin
import time

data = Pin(23, Pin.OUT) # SER (serial data input)
latch = Pin(22, Pin.OUT) # RCLK (storage register clock input)
clock = Pin(21, Pin.OUT) # SRCLK (shift register clock input)
srclr = Pin(19, Pin.OUT) # SRCLR (clear register)

TOTAL_STATIONS = 200

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

def enable_station_lights(station_ids):
    station_ids_set = set(station_ids)
    
    for station_id in range(TOTAL_STATIONS - 1, -1, -1):
        if station_id in station_ids_set:
            shift_bit(1)
        else:
            shift_bit(0)

    update_register()

