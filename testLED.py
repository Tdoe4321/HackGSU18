import mraa, time

gpio_1 = mraa.Gpio(27)

gpio_1.dir(mraa.DIR_OUT)
while True:
    gpio_1.write(1);


