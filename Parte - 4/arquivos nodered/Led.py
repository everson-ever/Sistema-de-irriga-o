import RPi.GPIO as GPIO    
import time

vermelhor = 11
verde = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(vermelhor,GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)


class Led:


    def ligar(self, led):
        GPIO.output(led, 1)

    def desligar(self, led):
        GPIO.output(led, 0)
