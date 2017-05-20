# *******************************************************************
# *  FUNCTION TO CALCULATE THE DISTANCE FROM OBSTRUCTIONS IN FRONT  *
# *******************************************************************
# *        THIS USES THE HC-SR04 ULTRASONIC DISTANCE SENSOR         *
# *******************************************************************
# * Unfortunately, the HC-SR04 suffers from some inherent built-in  *
# * flaws, particularly if the reflected sound waves bounce off     *
# * objects at a distance and/or at oblique angles.  This results   *
# * in very erratic signals being generated on the 'Echo' pin.      *
# * Since we're only interested in short distances up to 20cm, we   *
# * need to trap these errors within this function, otherwise the   *
# * program would be very slow to respond to the Wii Remote buttons.*
# * In worst-case situations the program could simply 'hang' whilst *
# * waiting for an echo signal which never ends!  On exit, if a     *
# * valid short distance is calculated, then 'distance' contains    *
# * the value in centimetres.  If a sensor error occurs, then a     *
# * value of 100 is returned instead.                               *
# *******************************************************************
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
trig = 38
echo = 40
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def get_distance ():
    global trig, echo                                                   # Allow access to 'trig' and 'echo' constants

    if GPIO.input (echo):                                               # If the 'Echo' pin is already high
        return (100)                                                    # then exit with 100 (sensor fault)

    distance = 0                                                        # Set initial distance to zero

    GPIO.output (trig,False)                                            # Ensure the 'Trig' pin is low for at
    time.sleep (0.05)                                                   # least 50mS (recommended re-sample time)

    GPIO.output (trig,True)                                             # Turn on the 'Trig' pin for 10uS (ish!)
    dummy_variable = 0                                                  # No need to use the 'time' module here,
    dummy_variable = 0                                                  # a couple of 'dummy' statements will do fine
    
    GPIO.output (trig,False)                                            # Turn off the 'Trig' pin
    time1, time2 = time.time(), time.time()                             # Set inital time values to current time
    
    while not GPIO.input (echo):                                        # Wait for the start of the 'Echo' pulse
        time1 = time.time()                                             # Get the time the 'Echo' pin goes high
        if time1 - time2 > 0.02:                                        # If the 'Echo' pin doesn't go high after 20mS
            distance = 100                                              # then set 'distance' to 100
            break                                                       # and break out of the loop
        
    if distance == 100:                                                 # If a sensor error has occurred
        return (distance)                                               # then exit with 100 (sensor fault)
    
    while GPIO.input (echo):                                            # Otherwise, wait for the 'Echo' pin to go low
        time2 = time.time()                                             # Get the time the 'Echo' pin goes low
        if time2 - time1 > 0.02:                                        # If the 'Echo' pin doesn't go low after 20mS
            distance = 100                                              # then ignore it and set 'distance' to 100
            break                                                       # and break out of the loop
        
    if distance == 100:                                                 # If a sensor error has occurred
        return (distance)                                               # then exit with 100 (sensor fault)
        
                                                                        # Sound travels at approximately 2.95uS per mm
                                                                        # and the reflected sound has travelled twice
                                                                        # the distance we need to measure (sound out,
                                                                        # bounced off object, sound returned)
                                                                        
    distance = (time2 - time1) / 0.00000295 / 2 / 10                    # Convert the timer values into centimetres
    return (distance) 
