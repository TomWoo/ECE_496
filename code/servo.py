import RPi.GPIO as GPIO
import time

pinOut = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinOut, GPIO.OUT)

p = GPIO.PWM(pinOut, 500)
p.start(7.5)

try:
	while True:
		# GPIO.output(pinOut, 1)
		# time.sleep(0.0015)
		# GPIO.output(pinOut, 0)

		# time.sleep(2)

                '''
                p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		time.sleep(1)
                '''
                p.ChangeDutyCycle(1)
                time.sleep(0.1)

except KeyboardInterrupt:
        p.stop()
	GPIO.cleanup()
