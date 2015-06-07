#
# HeatTest.py
# Josh Artuso
#
# Test the heat sensor
#

import Sensors
import requests
import json
import datetime
import time
import sys


def main(fire_fighter_id, sensor_id):
    """
    The main the function
    :return:
    """
    heat_sensor = Sensors.HeatSensor()

    while True:
        if heat_sensor.device_exists():
            raw_data = heat_sensor.read_temp_raw()
            temp = heat_sensor.calculate_temperature(raw_data)[1]
            time_stamp = datetime.datetime.now()
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            print temp
            data_dict = {"sensor": sensor_id,
                    "firefighter": fire_fighter_id,
                    "measurement_object": 1,
                    "value": temp,
                    "timestamp": str(time_stamp)}

            response = requests.post("http://192.168.1.1:5001/api/reading", data=json.dumps(data_dict), headers=headers)
            print response

            time.sleep(1)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print "Usage: HeatTest <fire_fighter_id> <sensor_id>"
