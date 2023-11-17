from machine import Pin
import time

TOTAL_STATIONS = 200

class SR_74hc595:
    def __init__(self):
        self.data = Pin(23, Pin.OUT) # SER (serial data input)
        self.latch = Pin(22, Pin.OUT) # RCLK (storage register clock input)
        self.clock = Pin(21, Pin.OUT) # SRCLK (shift register clock input)
        self.srclr = Pin(19, Pin.OUT) # SRCLR (clear register)

        self.clear_register()

    def shift_bit(self, value):
        self.data.value(value)
        self.clock.value(1)
        self.clock.value(0)

    def update_register(self):
        self.latch.value(1)
        self.latch.value(0)

    def clear_register(self):
        self.srclr.value(0)
        self.srclr.value(1)

        self.update_register()

    def enable_station_lights(self, station_ids):
        station_ids_set = set(station_ids)
        
        for station_id in range(TOTAL_STATIONS - 1, -1, -1):
            if station_id in station_ids_set:
                self.shift_bit(1)
            else:
                self.shift_bit(0)

        self.update_register()

