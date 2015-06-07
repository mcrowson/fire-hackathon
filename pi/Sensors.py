#
# Sensors.py
# Josh Artuso
#
# Handle Sensors
#

import glob
import time
import os


class HeatSensor:
    BASE_DIR = "/sys/bus/w1/devices/"
    DEVICE_FOLDER = glob.glob(BASE_DIR + "28*")[0]
    DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'

    def __init__(self):
        pass

    def device_exists(self):
        """
        Check if the device exists or nah
        :return: If the file exists
        """
        return os.path.isfile(self.DEVICE_FILE)

    def read_temp_raw(self):
        """
        Read the data from the file
        :return lines: The data from the file
        """
        f = open(self.DEVICE_FILE, "r")
        lines = f.readlines()
        f.close()
        return lines

    def calculate_temperature(self, raw_temp):
        """
        Calculate the temperature in fahrenheit
        :param raw_temp: The raw temp data from the sensor
        :return temp_c, temp_f: The temperature in fahrenheit and the other thing
        """
        while raw_temp[0].strip()[-3:] != 'YES':
            time.sleep(0.2)

        equals_pos = raw_temp[1].find('t=')

        if equals_pos != -1:
            temp_string = raw_temp[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
