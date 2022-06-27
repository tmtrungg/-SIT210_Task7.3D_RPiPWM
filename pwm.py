import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 4
GPIO_ECHO = 18
buzzerpin = 27

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(buzzerpin,GPIO.OUT)

GPIO.output(buzzerpin,True)
buzzer = GPIO.PWM(buzzerpin,0.1)
buzzer.start(1)
print("PWM set up...")

def distance():
    print("Measuring...")
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER,False)

    start = time.time()
    end = time.time()

    while (GPIO.input(GPIO_ECHO) == 0):
        start = time.time()
    while (GPIO.input(GPIO_ECHO) == 1):
        end = time.time()
        
    duration = end - start
    distance = duration*17000
    print("Measure done")
    return distance

def frequency(distances):
    if distances > 16 :
        return 0.25
    if distances > 12 and distances < 16 : 
        return 1
    if distances > 8 and distances < 12 : 
        return 2
    if distances > 4 and distances < 8 : 
        return 3
    if distances > 0 and distances < 4 :
        return 5
    else :
        return 0.25
try:
    while 1 :
        distanceoutput = distance()
        print("Distance : ")
        print(distanceoutput)
        print("cm")
        frequencyoutput = frequency(distanceoutput)
        buzzer.ChangeFrequency(frequencyoutput)
        time.sleep(5)
except KeyboardInterrupt:
        GPIO.cleanup()
        buzzer.stop()
