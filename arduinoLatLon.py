import serial, time, geocoder, json, subprocess
from GPIOLibrary import GPIOProcessor
ard = serial.Serial('/dev/tty96B0', 9600)
crash = False
ardOut = None
data = {}

GP = GPIOProcessor()
Pin27 = GP.getPin27()

if __name__ == '__main__':
    print("Welcome to the Crash Report Sensor!")
    Pin27.out()
    try:
        while True:
            ardOut = ard.readline()
            ardOut = int(ardOut)
            if(ardOut == 0):
                crash = False
                ardOut = None
                Pin27.low()
            if(crash == False and ardOut == 1):
                latlon = geocoder.ip('me').latlng
                print(latlon)
                crash = True

                Pin27.high()

                data['lat'] = []
                data['lat'].append({
                    'val': latlon[0]
                })
                data['lon'] = []
                data['lon'].append({
                    'val': latlon[1]    
                })
                with open('/home/linaro/HackGSU18/data.json', 'w') as outfile:
                    json.dump(data, outfile)
                
                subprocess.call("scp /home/linaro/HackGSU18/data.json root@142.93.73.155:/var/www/html", shell=True)


    except KeyboardInterrupt:
        GP.cleanup()
        print("CTRL-C!! Exiting...")
