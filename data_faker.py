__author__ = 'matthew'

import random
import requests


def tank_remaining():
    readings = [1.0]
    for i in range(100):
        previous = readings[-1]
        next = previous - random.gauss(0.04, 0.05)
        readings.append(next)

faked_measurements = {
    'oxygen_in_tank': tank_remaining(),
    'heart_rate': [random.gauss(110, 8) for x in range(100)],
}

for i in range(100):
    requests.post('http://127.0.0.1:5001/api/reading',
                  )

