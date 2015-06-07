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


def main():
    """
    The main the function
    :return:
    """
    heat_sensor = Sensors.HeatSensor()

    if heat_sensor.device_exists():
        raw_data = heat_sensor.read_temp_raw()
        temp = heat_sensor.calculate_temperature(raw_data)[1]
        time_stamp = datetime.datetime.now()
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        print temp
        data_dict = {"id": 1,
                "sensor": 1,
                "firefighter": 1,
                "measurement_object": 1,
                "value": temp,
                "timestamp": str(time_stamp)}

        response = requests.post("http://192.168.1.1:5001/api/reading", data=json.dumps(data_dict), headers=headers)
        print response


if __name__ == "__main__":
    main()
