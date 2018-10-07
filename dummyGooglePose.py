from geolocation.main import GoogleMaps
import time
import json, subprocess

data = {}

start = time.time()

while True:
    if(time.time() - start < 10):
	address = 'New York City Wall Street 12'
        time.sleep(2)
    elif(time.time() - start > 10 and time.time() < 20):
    	address = 'New York City Wall Street 12'
        time.sleep(2)
    elif(time.time() - start > 20 and time.time() < 30):
    	address = 'New York City Wall Street 12'
        time.sleep(2)
    elif(time.time() > 30):
    	start = time.time()
    	
    google_maps = GoogleMaps(api_key = 'AIzaSyCqBaEO3JOEwpdTb31ImhXBU6t_7KBJWT8')

    location_info = google_maps.search(address)
    location_info = location_info.first()

    print location_info.all() # return list of all location.

    data['lat'] = []
    data['lat'].append({
        'val': location_info.lat
    })
    data['lon'] = []
    data['lon'].append({
        'val': location_info.lng    
    })


    with open('/home/linaro/HackGSU18/data.json', 'w') as outfile:
    	json.dump(data, outfile)
                
    subprocess.call("scp /home/linaro/HackGSU18/data.json root@142.93.73.155:/var/www/html", shell=True)
