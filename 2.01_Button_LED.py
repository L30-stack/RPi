import RPi.GPIO as GPIO

ledPin=11
buttonPin=12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    current=0
    print('LED off')
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            if current==0:
                current=1
                print('LED on')
            if current==1:
                current=0
                print('LED off')
        else:
            if current==0:
                GPIO.output(ledPin,GPIO.LOW)
            if current==1:
                GPIO.output(ledPin,GPIO.HIGH)
    
def destroy():
    GPIO.output(ledPin,GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program gestartet...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()