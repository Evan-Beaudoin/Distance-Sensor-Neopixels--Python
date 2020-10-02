# Add your Python code here. E.g.
# Created by: Evan
# Date: Oct.2020

#This program uses the ultrasonic sensor to change the color of the neopixels at certain distances

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin16, 4)


class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    #   returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(baudrate=125000, sclk=self.sclk_pin,
                 mosi=self.trigger_pin, miso=self.echo_pin)
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next((ind, v)
                                for ind, v in enumerate(resp[i:length - 2]) if resp[i + ind + 1] == 0)
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist= -1 if i < 0 else round(((pre + (k - i) * 8. + post) * 8 * 0.172) / 2)
        return dist
        
    
sonar = HCSR04()

while True:
    
    display.show(sonar.distance_mm())
    
    
    if sonar.distance_mm() > 40:
          np.clear()
          np[3] = (0, 255, 0)
          np[2] = (0, 255, 0)
          np[1] = (0, 255, 0)
          np[0] = (0, 255, 0)
          np.show()
          
    elif sonar.distance_mm() <= 40 and sonar.distance_mm() > 10 :
          np.clear()
          np[3] = (0, 0, 255)
          np[2] = (0, 0, 255)
          np[1] = (0, 0, 255)
          np[0] = (0, 0, 255)
          np.show()
          
          if sonar.distance_mm() <= 39 and sonar.distance_mm() >= 30 :
           np.clear()
           np[3] = (0, 0, 255)
           np[2] = (0, 0, 255)
           np[1] = (0, 0, 255)
           np.show()
           
          elif sonar.distance_mm() <= 29 and sonar.distance_mm() >= 20 :
           np.clear()
           np[3] = (0, 0, 255)
           np[2] = (0, 0, 255)
           np.show()
          
    else:
          np.clear()
          np[3] = (255, 0, 0)
          np[2] = (255, 0, 0)
          np[1] = (255, 0, 0)
          np[0] = (255, 0, 0)
          np.show()
          
          
    sleep(100)    
    
          
       
          



    
    
    
