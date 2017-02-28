import time
import pigpio
from wavePWM import PWM

pi = pigpio.pi()

pins = [4, 14, 15, 18]
freqs = [500, 400, 300, 200] #[500, 555, 625, 715]
#p = [PWM(pi, 500), PWM(pi, 555), PWM(pi, 625), PWM(pi, 715)]
pwm = PWM(pi)

while True:
    for i in range(len(pins)):
        pin = pins[i]
        pi.set_mode(pin, pigpio.OUTPUT)
        ##pi.hardware_PWM(pin, 500-10*i, 250000+100000*i)

        raw_input('Press enter to continue (' + str(i) + ')')
        
        #pwm = p[i]
        pwm.set_frequency(freqs[i])
        T = pwm.get_cycle_length()
        pwm.set_pulse_start_in_micros(pin, T/10+1000*i)
        pwm.set_pulse_length_in_micros(pin, 100*i)
        print(pwm.get_frequency())
    pwm.update()
    
        #pi.set_PWM_frequency(pins[0], 100)
        #print(pi.get_PWM_frequency(pins[0]))
