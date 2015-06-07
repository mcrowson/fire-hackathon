#
# DataSender.py
# Josh Artuso
#
# This file will collect data from the sensors that we have and simulate the rest.
# The collection of data is then sent back to the API
# The simulated data was stolen from Matthews data_faker.py. No Shame.
#

import sys
import Sensors
import time
import requests
import json
import random


def tank_remaining(x):
    readings = [100]
    for i in range(100):
        previous = readings[-1]
        rand = random.random()
        if rand > x:
            next = previous - 1
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


def main(url, fire_fighter_id, heat_sensor_id):
    """

    :param url:
    :param fire_fighter_id:
    :param heat_sensor_id:
    :return:
    """
    heat_sensor = Sensors.HeatSensor()

    while True:
        for i in range(35):

            if not heat_sensor.device_exists():
                return

            raw_data = heat_sensor.read_temp_raw()
            temp = heat_sensor.calculate_temperature(raw_data)[1]
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            print temp

            # Temperature
            data = {"sensor": heat_sensor_id,
                    "firefighter": fire_fighter_id,
                    "measurement_object": 1,
                    "value": temp,
                    "timestamp": time.strftime('%m/%d/%Y %H:%M:%S')
                    }

            requests.post(url, data=json.dumps(data), headers=headers)

            # Kind of a hack here...
            # The sensor ids need to be unique but we have multiple firefighters..
            # I am going to subtract 1 from the sensor id and then add fire_fighter_id to it...
            # Again, its a hack and I am not proud of this.
            # I am sure that once I get some sleep and wake up refreshed I will hate myself for this.
            # I've been doing this for 17 hours straight now so thats my excuse.

            # Oxygen in tank
            data = {'value': faked_measurements1['oxygen_in_tank'][i],
                    'firefighter': fire_fighter_id,
                    'sensor': (3-1) + int(fire_fighter_id),
                    'measurement_object': 2,
                    'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                    }

            requests.post(url, headers=headers, data=json.dumps(data))

            # Heart rate
            data = {'value': faked_measurements1['heart_rate'][i],
                    'firefighter': fire_fighter_id,
                    'sensor': (4-1) + int(fire_fighter_id),
                    'measurement_object': 3,
                    'timestamp': time.strftime('%m/%d/%Y %H:%M:%S')
                    }

            requests.post(url, headers=headers, data=json.dumps(data))

            '''
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
            '''

            time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "Usage: DataSender.py <api_host:port> <fire_fighter_id> <heat_sensor_id>"
