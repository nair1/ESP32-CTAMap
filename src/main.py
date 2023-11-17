import wifi.wifi as wifi
from shift_register_modules.SR_74hc595 import SR_74hc595
import urequests

wifi.connect_to_wifi()

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = urequests.get(api_url)
print("API Response:")
print(response.text)

shift_register = SR_74hc595()
shift_register.enable_station_lights([0, 2, 4, 6])