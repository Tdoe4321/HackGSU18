import serial, time, geocoder
ard = serial.Serial('/dev/tty96B0', 9600)
crash = False
ardOut = None


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
                print(geocoder.ip('me').latlng)
                crash = True
                #time.sleep(1)
            


    except KeyboardInterrupt:
        print("CTRL-C!! Exiting...")
