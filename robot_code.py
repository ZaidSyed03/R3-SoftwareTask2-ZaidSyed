import curses # This imports curses library
import RPi.GPIO as GPIO 

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)


screen = curses.initscr()
curses.noecho() # Allows keys to be "echoed" into window 
curses.cbreak() # This willallow the key to be registeed without pressing enter key
screen.keypad(True) # while this is true execute the below loop

try:
        while True:   
            char = screen.getch() #this is the first vheck that is done in the loop if key "l" is pressed the "finally" command will excute if not it will continue below
            if char == ord('l'):
                break
            elif char == curses.KEY_UP: # the program will check if the "up" key along with the other keys are pressed and then execute the code associated with the pressed key 
                print ("Moving Forward");
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
                
            elif char == curses.KEY_RIGHT:
                print ("Turning Right");
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                
            elif char == curses.KEY_DOWN:
                print ("Going backwards, I may run u over cuz im not a smart car");
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                
            elif char == curses.KEY_LEFT:
                print ("Turning Left");
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo() #Cneeded to terminate curses library properly
    curses.endwin()   #Restores terminal to orginal operating mode
    GPIO.cleanup()    #resets GPIO pins