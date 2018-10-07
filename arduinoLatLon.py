import serial, time, geocoder, json
ard = serial.Serial('/dev/tty96B0', 9600)
crash = False
ardOut = None
data = {}

#import geocoder
#g = geocoder.ip('me')
#print(g.latlng)

if __name__ == '__main__':
    print("Welcome to the Crash Report Sensor!")
    try:
        while True:
            ardOut = ard.readline()
            ardOut = int(ardOut)
            if(ardOut == 0):
                crash = False
                ardOut = None
            if(crash == False and ardOut == 1):
                latlon = geocoder.ip('me').latlng
                print(latlon)
                crash = True

                data['lat'] = []
                data['lat'].append({
                    'val': latlon[0]
                })
                data['lon'] = []
                data['lon'].append({
                    'val': latlon[1]    
                })
                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile)
                #time.sleep(1)
            


    except KeyboardInterrupt:
        print("CTRL-C!! Exiting...")
