import requests
import json

def autocomplete_address(input_name):
    url = "https://api.locationiq.com/v1/autocomplete.php"

    data = {
        'key': '36893c8f7e7af9',
        'q': input_name + 'Reading England',
        #51.4931000, -0.9412000, 51.4595000, -1.0080000
        'viewbox': '-0.9412000, 51.4931000, -1.0080000, 51.4595000'
    }

    addresses = []
    response = requests.get(url, params=data)

    for i in json.loads(response.text):
        if (float(i['lat']) > 51.4595000) and (float(i['lat']) < 51.4931000) and (float(i['lon']) > -1.0080000) and (float(i['lon']) < -0.9412000):
            addresses.append(i['display_name'])

    return addresses
