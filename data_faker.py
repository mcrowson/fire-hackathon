__author__ = 'matthew'

import random
import time
import requests
import json


def tank_remaining(x):
    readings = [100]
    for i in range(100):
        previous = readings[-1]
        rand = random.random()
        if rand > x:
            next = previous-1
        else:
            next = previous
        readings.append(next)
    return readings

faked_measurements1 = {
    'oxygen_in_tank': tank_remaining(0.6),
    'heart_rate': [int(random.gauss(110, 8)) for x in range(35)],
}

faked_measurements2 = {
    'oxygen_in_tank': tank_remaining(0.4),
    'heart_rate': [int(random.gauss(120, 12)) for x in range(35)],
}

url = 'http://127.0.0.1:5001/api/reading'
headers = {'content-type': 'application/json'}
cont = True
while cont:
    for i in range(35):
        data = {'value': faked_measurements1['oxygen_in_tank'][i],
                'firefighter': 1,
                'sensor': 3,
                'measurement_object': 2,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }
        requests.post(url, headers=headers, data=json.dumps(data))


        data = {'value': faked_measurements1['heart_rate'][i],
                'firefighter': 1,
                'sensor': 4,
                'measurement_object': 3,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }

        requests.post(url, headers=headers, data=json.dumps(data))

        data = {'value': faked_measurements2['oxygen_in_tank'][i],
                'firefighter': 2,
                'sensor': 5,
                'measurement_object': 2,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }
        requests.post(url, headers=headers, data=json.dumps(data))


        data = {'value': faked_measurements2['heart_rate'][i],
                'firefighter': 2,
                'sensor': 6,
                'measurement_object': 3,
                'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                }

        requests.post(url, headers=headers, data=json.dumps(data))
        time.sleep(1)

