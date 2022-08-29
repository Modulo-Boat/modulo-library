import redis
import json

class Gps:
  def __init__(self, redis):
    pubsub = redis.pubsub()
    pubsub.psubscribe(**{'gps_*': self._subscribe})
    thread = pubsub.run_in_thread(sleep_time=0.001)
    self.message = None

    self._latitude = None
    self._longitude = None
    self._altitude = None
    self._speed = None
    self._true_course = None

  def _subscribe(self, message):
    if message['channel'] == b'gps_longitude':
      self._longitude = float(message['data'])
    elif message['channel'] == b'gps_latitude':
      self._latitude = float(message['data'])
    elif message['channel'] == b'gps_altitude':
      self._altitude = float(message['data'])
    elif message['channel'] == b'gps_speed':
      self._speed = float(message['data'])
    elif message['channel'] == b'gps_true_course':
      self._true_course = float(message['data'])

  @property
  def latitude(self):
    return self._latitude

  @property
  def longitude(self):
    return self._longitude

  @property
  def altitude(self):
    return self._altitude

  @property
  def speed(self):
    return self._speed

  @property
  def true_course(self):
    return self._true_course
