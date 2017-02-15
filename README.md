# ECE_496

TODO:
* order parts
* document wireless motor control set-up (RadioHead library) and power consumption -- rx redundancy?
* custom boards?
* schematics in EAGLE
* set up Raspi
* sonar amplifier w/ sound card?
* epoxy test RF modules
* search algorithm!

Wireless motor control
* 433 MHz RF modules -- ASK modulation
* Arduino RadioHead library (need to find a Raspi equivalent) provides a transmission protocol w/ CRC checksums
* Need to implement unique slave (motor) addressing, as well as 8-bit PWM resolution signaling (two bytes in total per payload)
* Need to characterize the transmitter's power consumption (8 mA at 3.3 V seems to be more than enough for a worst-case range of 1 m)
