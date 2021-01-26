import requests
import json

def getGeoCode(input_name):
    url = "https://eu1.locationiq.com/v1/search.php"

    data = {
        'key': '36893c8f7e7af9',
        'q': input_name + 'Reading England',
        'format': 'json'
    }

    response = requests.get(url, params=data)

    print(response.text)

    return (float(json.loads(response.text)[0]['lat']), float(json.loads(response.text)[0]['lon']))

print(getGeoCode("Waitrose Church Street"))
