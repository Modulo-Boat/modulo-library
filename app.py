from re import A
import math
from modulo import Modulo
import time

boat = Modulo('127.0.0.1')

# imu = boat.imu

# filtered_heading_rad = 0
# while 1:
#   ax = imu.accelerometer.x
#   ay = imu.accelerometer.y
#   az = imu.accelerometer.z
#   hx = imu.compass.x
#   hy = imu.compass.y
#   hz = imu.compass.z
#   if (ax != None and ay != None and ax != None and hx != None and hy != None and hz != None):
#     a = (ax**2 + ay**2 + az**2)**0.5
#     ax/=a
#     ay/=a
#     az/=a
#     h = (hx**2 + hy**2 + hz**2)**0.5
#     hx/=h
#     hy/=h
#     hz/=h
#     pitch_rad = math.asin(ax)
#     roll_rad = math.asin(-ay/math.cos(pitch_rad))
#     yaw_rad = math.atan2(hz * math.sin(roll_rad) - hy * math.cos(roll_rad), hx * math.cos(pitch_rad) + hy * math.sin(pitch_rad) * math.sin(roll_rad) + hz * math.sin(pitch_rad) * math.cos(roll_rad))
#     heading_rad = yaw_rad % (2 * math.pi)
#     if heading_rad < 0:
#       heading_rad += 2 * math.pi
#     filtered_heading_rad = (filtered_heading_rad * 19 + heading_rad) / 20
#     print("pitch_rad:", pitch_rad*180/math.pi)
#     print("roll_rad:", roll_rad * 180 / math.pi)
#     print("yaw_rad:", yaw_rad * 180 / math.pi)
#     print("heading_rad:", heading_rad * 180 / math.pi);
#     print("filtered_heading_rad:", filtered_heading_rad * 180 / math.pi)
#     print("\n\n\n")
#     time.sleep(0.1)



boat.motor.left(0)
boat.motor.right(0)
time.sleep(1)


while 1:
  for i in range(0,100,1):
    boat.motor.left(i/100)
    print(i/100)
    time.sleep(0.1)
  for i in range(100,-100,-1):
    boat.motor.left(i/100)
    print(i/100)
    time.sleep(0.1)
  for i in range(-100,1,1):
    boat.motor.left(i/100)
    print(i/100)
    time.sleep(0.1)
  for i in range(0,100,11):
    boat.motor.right(i/100)
    print(i/100)
    time.sleep(0.1)
  for i in range(100,-100,-1):
    boat.motor.right(i/100)
    print(i/100)
    time.sleep(0.1)
  for i in range(-100,1,11):
    boat.motor.right(i/100)
    print(i/100)
    time.sleep(0.1)
