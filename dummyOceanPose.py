import serial, time, geocoder, json, subprocess
data = {}

if __name__ == '__main__':
    latlon = geocoder.ip('me').latlng

    data['lat'] = []
    data['lat'].append({
        'val': 23.5
    })
    data['lon'] = []
    data['lon'].append({
        'val': -80    
    })
    with open('/home/linaro/HackGSU18/data.json', 'w') as outfile:
        json.dump(data, outfile)
                
    subprocess.call("scp /home/linaro/HackGSU18/data.json root@142.93.73.155:/var/www/html", shell=True)
