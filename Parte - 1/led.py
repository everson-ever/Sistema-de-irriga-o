
import RPi.GPIO as GPIO    
import time                

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

def singleLed():
    try:
        while True:
            print("")
            print("Led vermelho: 1")
            print("Led verde: 2")
            print("Alternando: 3");
            order = input("Selecione uma ação: ")
            print("")
            if order == "1":
                GPIO.output(11, 1)
                GPIO.output(13, 0)
            elif order == "2":
                GPIO.output(13, 1)
                GPIO.output(11, 0)
            elif order == "3":
                twoLeds()
    except KeyboardInterrupt:
        GPIO.output(13, 0)
        GPIO.output(11, 0)
        GPIO.cleanup()
        print("")

def twoLeds():
    print("CTRL + C para sair do alternar!")
    try:
        while True:
            GPIO.output(11, 1)
            time.sleep(0.4)
            GPIO.output(11, 0)
            GPIO.output(13, 1)
            time.sleep(0.4)
            GPIO.output(13, 0)
    except KeyboardInterrupt:
        singleLed()

singleLed()



    






