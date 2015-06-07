__author__ = 'matthew'

import random
import time
import requests
import json


def tank_remaining():
    readings = [100]
    for i in range(100):
        previous = readings[-1]
        rand = random.random()
        if rand > 0.6:
            next = previous-1
        else:
            next = previous
        readings.append(next)
    return readings

faked_measurements = {
    'oxygen_in_tank': tank_remaining(),
    'heart_rate': [int(random.gauss(110, 8)) for x in range(35)],
}

url = 'http://127.0.0.1:5001/api/reading'
headers = {'content-type': 'application/json'}
cont = True
while cont:
    for i in range(35):
        data = {'value': faked_measurements['oxygen_in_tank'][i],
                'firefighter': 1,
                'sensor': 1,
                'measurement_object': 1,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }
        requests.post(url, headers=headers, data=json.dumps(data))


        data = {'value': faked_measurements['heart_rate'][i],
                'firefighter': 1,
                'sensor': 1,
                'measurement_object': 1,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }

        requests.post(url, headers=headers, data=json.dumps(data))
        time.sleep(1)

