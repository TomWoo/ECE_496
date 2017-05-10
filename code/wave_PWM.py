#!/usr/bin/env python

import time
import pigpio

# wave_PWM.py
# 2016-03-19
# Public Domain

"""
This script shows how to use waves to generate PWM with a
set frequency on any spare GPIO.

Note that only one wave can be transmitted at a time.  So if
waves are being used to generate PWM they can't also be used
at the same time for another purpose.

The frequency is defined by the number of cycles per second.

A wave is generated of length 1000000/frequency microseconds.
The GPIO are switched on and off within the wave to set the
duty cycle for each GPIO.  The wave is repeatedly transmitted.

Waves have a resolution of one microsecond.

You will only get the requested frequency if it divides
exactly into 1000000.

For example, suppose you want a frequency of 7896 cycles per
second.  The wave length will be 1000000/7896 or 126 (for an
actual frequency of 7936.5) and there will be 126 steps
between off and fully on.

One function is provided:

set_dc(channel, dc)

channel: is 0 for the first GPIO, 1 for the second, etc.
     dc: is the duty cycle which must lie between 0 and the
         number of steps.
"""

FREQ=500 # The PWM cycles per second.

PWM1=12
PWM2=16
PWM3=20
PWM4=21

GPIO=[PWM1, PWM2, PWM3, PWM4]

_channels = len(GPIO)

_dc=[0]*_channels

_micros=1000000/FREQ

old_wid = None

def set_dc(channel, dc):

   global old_wid

   if dc < 0:
      dc = 0
   elif dc > _micros:
      dc = _micros

   _dc[channel] = dc

   for c in range(_channels):
      d = _dc[c]
      g = GPIO[c]
      if d == 0:
         pi.wave_add_generic([pigpio.pulse(0, 1<<g, _micros)])
      elif d == _micros:
         pi.wave_add_generic([pigpio.pulse(1<<g, 0, _micros)])
      else:
         pi.wave_add_generic(
            [pigpio.pulse(1<<g, 0, d), pigpio.pulse(0, 1<<g, _micros-d)])

   new_wid = pi.wave_create()

   if old_wid is not None:

      pi.wave_send_using_mode(new_wid, pigpio.WAVE_MODE_REPEAT_SYNC)

      # Spin until the new wave has started.
      while pi.wave_tx_at() != new_wid:
         pass

      # It is then safe to delete the old wave.
      pi.wave_delete(old_wid)

   else:

      pi.wave_send_repeat(new_wid)

   old_wid = new_wid

pi = pigpio.pi()
if not pi.connected:
   exit(0)

# Need to explicity set wave GPIO to output mode.

for g in GPIO:
   pi.set_mode(g, pigpio.OUTPUT)

#for i in range(_micros):

#set_dc(0, i)
#set_dc(1, i+(_micros/4))
#set_dc(2, (_micros/4)-i)
#set_dc(3, _micros-i)

def calibrate():
   for i in range(4):
      print('Calibrating ESC ' + str(i) + '\n')

      set_dc(i, _micros*0.5)
      print('dc is now set to neutral...\n')
      
      raw_input('Press enter to set to forward...\n')
      for j in range(200):
         set_dc(i, _micros*(0.5+j*0.2/200))
         time.sleep(0.001)
         
      raw_input('Press enter to set to backward...\n')
      for j in range(400):
         set_dc(i, _micros*(0.7-j*0.2/200))
         time.sleep(0.001)
         
      raw_input('DONE. Press enter to continue...\n')
      set_dc(i, _micros*0.4)

#dc = 0.08
#def run(dc):

#calibrate()

while True:
   #for i in range(4):
   #dc = 0.5
   #set_dc(i, _micros*dc)
   set_dc(0, _micros*0.0) #back
   set_dc(1, _micros*0.0) #left
   set_dc(2, _micros*0.50) #right
   set_dc(3, _micros*0.50) #front
   
   time.sleep(3)

pi.wave_tx_stop()

if old_wid is not None:
   pi.wave_delete(old_wid)

pi.stop()

#calibrate()
#run(0.4)
#stop()
