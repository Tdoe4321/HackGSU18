import serial, time, geocoder, json, subprocess
data = {}

if __name__ == '__main__':
    address  = raw_input("Enter Address: ")
    g = geocoder.google('Mountain View, CA')

    print(g.latlng)

    data['lat'] = []
    data['lat'].append({
        'val': g.latlng[0]
    })
    data['lon'] = []
    data['lon'].append({
        'val': g.latlng[1]    
    })
    with open('/home/linaro/HackGSU18/data.json', 'w') as outfile:
        json.dump(data, outfile)
                
    subprocess.call("scp /home/linaro/HackGSU18/data.json root@142.93.73.155:/var/www/html", shell=True)
