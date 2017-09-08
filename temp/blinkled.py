import RPi.GPIO as GPIO
import time
 
LedPin = 11    # pin22
 
def setup():
        GPIO.setmode(GPIO.BOARD)       # Set the board mode to numbers pins by physical location
        GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
        GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
 
def flash():
                GPIO.output(LedPin, GPIO.LOW)   # led on
                time.sleep(5)                 # wait 1 sec
                GPIO.output(LedPin, GPIO.HIGH)  # led off
		destroy()
def destroy():
 
        GPIO.output(LedPin, GPIO.HIGH)     # led off
        GPIO.cleanup()                     # Release resource
 
if __name__ == '__main__':     # Program start from here
        setup()
        try:
                flash()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the destroy() will be  executed.
                destroy()
