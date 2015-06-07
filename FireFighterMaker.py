import requests
import json
import time

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
dob = time.strftime('%m/%d/%Y %H:%M:%S')
data_dict = {"first_name": "jimmy",
             "last_name": "billy",
             "dob": dob,
             "baseline_resting_heartrate": 60,
             "baseline_active_heartrate": 100,
             "height": 300,
             "weight": 160}

response = requests.post("http://localhost:5001/api/firefighter", data=json.dumps(data_dict), headers=headers)
print(response.json())

data_dict = {"first_name": "james",
             "last_name": "brown",
             "dob": dob,
             "baseline_resting_heartrate": 63,
             "baseline_active_heartrate": 12,
             "height": 399,
             "weight": 180}

response = requests.post("http://localhost:5001/api/firefighter", data=json.dumps(data_dict), headers=headers)
print(response.json())

#'http://localhost:5001/api/reading?q={"filters":[{"name":"firefighter","op":"eq","val":1},{"name":"measurement_object","op":"eq","val":1}],"order_by":[{"field":"id","direction":"desc"}]}' \
#'q={"filters":[{"name":"firefighter","op":"eq","val":2}]}'