import signal
import sys
import RPi.GPIO as GPIO


#GPIO 0,2,3,4 
#upB = Button(0, pull_up=True, bounce_time=1.0)
upB = 27
downB = 2
enterB = 3
backB = 4
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

currPos=0
def getCurPos():
    global currPos
    return currPos
def upFunc(channel):
    global currPos
    print("up",currPos)
    
    if(currPos>=0 and currPos<=8):
        currPos=currPos+1
    if (currPos>8):
        currPos =0
def downFunc(channelchannel):
    global currPos
    print("downB ",currPos)
    if(currPos>=0 and currPos<=8):
        currPos=currPos-1
    if (currPos<0):
        currPos =8
def enterFunc(channel):
    global currPos
    print("enter",currPos)
    
    
def backFunc(channel):
    
    print("back ", currPos)
    
    
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(upB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(upB, GPIO.BOTH, 
        callback=upFunc, bouncetime=100)

GPIO.setup(downB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(downB, GPIO.BOTH, 
        callback=downFunc, bouncetime=100)

GPIO.setup(enterB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(enterB, GPIO.BOTH, 
        callback=enterFunc, bouncetime=100)

GPIO.setup(backB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(backB, GPIO.BOTH, 
        callback=backFunc, bouncetime=100)
