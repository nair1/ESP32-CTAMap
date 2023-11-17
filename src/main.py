import wifi.wifi as wifi
import urequests

wifi.connect_to_wifi()

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = urequests.get(api_url)
print("API Response:")
print(response.text)