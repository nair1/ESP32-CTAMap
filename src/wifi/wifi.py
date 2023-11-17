import network
import time
from time import sleep

def connect_to_wifi():
    ssid = None
    password = None
    
    try:
        with open("config.env") as f:
            lines = f.read().splitlines()
            ssid = lines[0].split('=')[1].strip()
            password = lines[1].split('=')[1].strip()
    except OSError:
        print("Error reading config.env")
        return
    
    if not ssid or not password:
        return
    
    start_time = time.time()
    timeout = 30 # in seconds

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    wlan.connect(ssid, password)

    while not wlan.isconnected():
        elapsed_time = time.time() - start_time

        if elapsed_time > timeout:
            print("wifi connection timed out :(")
            return

        print("Connecting to wifi...")
        sleep(1)

    print("Connected to wifi")
    print("IP Address: ", wlan.ifconfig()[0])