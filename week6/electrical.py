

from machine import Pin, I2C 
from ssd1306 import SSD1306_I2C
import framebuf

WIDTH  = 128                                           
HEIGHT = 64                                             
i2c = I2C(0)                                           
                                                        
print("I2C Address      : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))            
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                 

# Raspberry Pi logo como 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Carga el raspberry pi logo en el framebuffer (la imagen es de 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

oled.text("help",5,5)    
oled.text("this is",5,15)         
oled.text("killing",5,35)       
oled.text("me",5,45)    
oled.show()



red=machine.Pin(13,machine.Pin.OUT)
yellow=machine.Pin(12,machine.Pin.OUT)
green=machine.Pin(11,machine.Pin.OUT)
ldr_sensor=machine.ADC(machine.Pin(28))
rtc=machine.RTC()
rtc.datetime((2023,3,16,11,2,0,0,0))

button =machine.Pin(6,machine.Pin.IN,machine.Pin.PULL_UP)
    

# Finalmente actualiza la pantalla oled para que se muestre la imagen y el texto
oled.show()
while True:
    print("Date",rtc.datetime())
    light_value=ldr_sensor.read_u16()
    print("light_intensity",light_value)
    print("\n\n")
    button_state=button.value()
    print("button_state",button_state)
    red.value(button_state)
    yellow.value(button_state)
    green.value(button_state)
        
