from machine import ADC,Pin
from machine import deepsleep
from utime import sleep

rled=Pin(16, Pin.OUT)
gled=Pin(25, Pin.OUT)
moisture=ADC(26)
sensor=Pin(27, Pin.OUT)

while True:
    gled.value(1)
    sensor.value(1)
    reading=moisture.read_u16()
    voltage=3300*reading/65535
    print("{:.1f}mV".format(voltage))
    if voltage<500:
        for i in range(50):
            rled.value(1)
            sleep(.5)
            rled.value(0)
            sleep(.5)
        sleep(10)
    
    else:
        sleep(60)
        
    print("I'm going to sleep now")
    
    gled.value(0)
    sensor.value(0)
    
    deepsleep(21540000)


    
