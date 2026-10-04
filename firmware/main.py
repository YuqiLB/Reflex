import time
from machine import Pin
import random

led = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP) #Pull up or down?

print("Start Program Now.")
print("Press the button to start!")
while 1:
    if button.value() == 0:
        print("Button Pressed!")
        break

while 1:
    led.off()
    print("Ready?")
    print("...")

    wait_time = random.uniform(1,5)

    timestart = time.ticks_ms()

    while (time.ticks_diff(time.ticks_ms(), timestart) < wait_time * 1000): #do not allow users to press button under the already determined random wait time.
        if (button.value() == 0):
            print("You pressed too early!")
            pressed_too_early = True

            while button.value() == 0: #must use a loop to ensure constant checking, using if statement only checks that instant
                pass
            break
    if (not pressed_too_early): #moved outside of the loop so that it doesn't have any delays
        led.on()
        timestart = time.ticks_ms()

        while button.value() == 1:
            pass
            # pass if the button is not pressed, loop until it is pressed
        timeend = time.ticks_ms()

        print("Rxn Time: ", time.ticks_diff(timeend, timestart), "ms")
        led.off()

    time.sleep(1)
    
    
