import requests
import time 
 

count = 0

while True:
    json_data = {}

    json_data['angle'] = count
    json_data['flag1'] = False
    json_data['flag2'] = True
    
    # time.sleep(1)
    
    try:
        # r = requests.post("http://192.168.43.200:5000/myCar", json=json_data)
        r = requests.post("http://10.11.39.10:5000/myCar", json=json_data)
        # r = requests.post("http://10.199.99.116:5000/myCar", json=json_data)
    
        print(json_data)

        count += 1
    except:
        print('device is off-line') 
  