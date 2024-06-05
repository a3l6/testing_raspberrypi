from machine import Pin
import utime


motor1a = Pin(20, Pin.OUT)
motor1b = Pin(19, Pin.OUT)

def forward():
    motor1a.high()
    motor1b.low()


def backward():
    motor1a.low()
    motor1b.high()

def stop():
    motor1a.low()
    motor1b.low()


def test():
    forward()
    utime.sleep(2)
    backward()
    utime.sleep(2)
    stop()

for i in range(5):
    print("Running")
    test()