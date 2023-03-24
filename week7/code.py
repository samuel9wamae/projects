import machine
import time
led=machine.Pin(13,machine.Pin.OUT)
while True:
    led.value(1)
    print("on")
    time.sleep(1.0)
    laed.value(0)
    print("off")
    time.sleep(0.5)