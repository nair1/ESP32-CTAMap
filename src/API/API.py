import requests
import json

API_URL = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx" 

def pretty_print_json(data):
    return json.dumps(data, indent=4)

def get_api_key():
    try:
        with open("src/config.env") as f:
            lines = f.read().splitlines()
            return lines[2].split('=')[1].strip()
    except OSError as e:
        print("Error reading config.env! Full stack trace: " + e)

def get_sample_data():
    api_key = get_api_key()

    params = {
        'key': api_key,
        'mapid': '40360',
        'outputType': 'JSON'
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        print(pretty_print_json(response.json()))
    else:
        print("Error:", response.status_code)

    response.close()

get_sample_data()