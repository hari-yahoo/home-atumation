import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servol = GPIO.PWM(11,50)

servol.start(0)
print("waiting for 2 seconds")
time.sleep(2)


duty = 2

while duty <= 12:
    servol.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

time.sleep(2)

print("Turning back to 90 degrees for 2 seconds")

servol.ChangeDutyCycle(7)
time.sleep(2)

print ("Turning back to 0 degrees")
servol.ChangeDutyCycle(2)
time.sleep(0.5)
servol.ChangeDutyCycle(0)

servol.stop()
GPIO.cleanup()
print("Goodbye")