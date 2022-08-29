from modulo import Modulo
import time

boat = Modulo('127.0.0.1')

boat.motor.left(0)
boat.motor.right(0)
time.sleep(1)
while True:
  for i in range(0, 100, 1):
    boat.motor.left(i/100)
    boat.motor.right(i/100)
    time.sleep(0.1)
  for i in range(100, -100, -1):
    boat.motor.left(i/100)
    boat.motor.right(i/100)
    time.sleep(0.1)
  for i in range(-100, 0, 1):
    boat.motor.left(i/100)
    boat.motor.right(i/100)
    time.sleep(0.1) 
