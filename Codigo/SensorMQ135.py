import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

try:
    while True:
        if GPIO.input(4):
            print("Normal")
        else:
            print("Â¡ALERTA! Niveles Anormales de Amoniaco. Favor de evacuar el area.")
        sleep(5)

finally:
    GPIO.cleanup()
