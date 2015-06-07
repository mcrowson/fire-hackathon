#
# HeatTest.py
# Josh Artuso
#
# Test the heat sensor
#

import Sensors


def main():
    """
    The main the function
    :return:
    """
    heat_sensor = Sensors.HeatSensor()

    if heat_sensor.device_exists():
        raw_data = heat_sensor.read_temp_raw()
        print heat_sensor.calculate_temperature(raw_data)[1]

if __name__ == "__main__":
    main()
