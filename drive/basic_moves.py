#!/usr/bin/python
import wiringpi2 as gpio
import time

#prepare PWM pins
gpio.wiringPiSetupGpio()
gpio.pinMode(12, gpio.GPIO.PWM_OUTPUT)
gpio.pinMode(13, gpio.GPIO.PWM_OUTPUT)

#prepare PWM channels
gpio.pwmSetMode(gpio.GPIO.PWM_MODE_MS)
gpio.pwmSetRange(480)
gpio.pwmSetClock(2)

#prepare direction pins
gpio.pinMode(5, gpio.GPIO.OUTPUT)
gpio.pinMode(6, gpio.GPIO.OUTPUT)

#movements
def straight_fw(speed):
  gpio.digitalWrite(5, 1)
  gpio.digitalWrite(6, 1)
  gpio.pwmWrite(12, speed)
  gpio.pwmWrite(13, speed)

def straight_bw(speed):
  gpio.digitalWrite(5, 0)
  gpio.digitalWrite(6, 0)
  gpio.pwmWrite(12, speed)
  gpio.pwmWrite(13, speed)

def stop():
  gpio.digitalWrite(5, 1)
  gpio.digitalWrite(6, 1)
  gpio.pwmWrite(12, 0)
  gpio.pwmWrite(13, 0)

def turn_180():
  gpio.digitalWrite(5, 0)
  gpio.digitalWrite(6, 1)
  gpio.pwmWrite(12, 300)
  gpio.pwmWrite(13, 300)
  time.sleep(2)
  stop() 

#playground
#straight_fw(300)
#time.sleep(2)
#stop()
#straight_bw(300)
#time.sleep(2)
#stop()
#turn_180()
