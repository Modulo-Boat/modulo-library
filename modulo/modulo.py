import redis
from .battery import Battery
from .gps import Gps
from .imu import Imu
from .motor import Motor



class Modulo():
  def __init__(self, ip):
    self._redis = redis.Redis(host=ip, port=30002)
    self.battery = Battery(self._redis)
    self.gps = Gps(self._redis)
    self.imu = Imu(self._redis)
    self.motor = Motor(self._redis)
    