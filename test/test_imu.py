from modulo import Modulo

boat = Modulo('192.168.1.109')

while True:
  print(boat.imu.heading)