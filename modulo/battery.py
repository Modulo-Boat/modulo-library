import redis
import json

class Battery:
  def __init__(self, redis):
    pubsub = redis.pubsub()
    pubsub.psubscribe(**{'battery_*': self._subscribe})
    thread = pubsub.run_in_thread(sleep_time=0.001)
    self.message = None

    self._percentage = None
    self._voltage = None
    self._capacity = None
    self._current = None
    self._remaining_sec = None

  def _subscribe(self, message):
    if message['channel'] == b'battery_percentage':
      self._percentage = float(message['data'])
    elif message['channel'] == b'battery_voltage':
      self._voltage = float(message['data'])
    elif message['channel'] == b'battery_capacity':
      self._capacity = float(message['data'])
    elif message['channel'] == b'battery_current':
      self._current = float(message['data'])
    elif message['channel'] == b'battery_remaining_sec':
      self._remaining_sec = float(message['data'])

  @property
  def percentage(self):
    return self._percentage

  @property
  def voltage(self):
    return self._voltage

  @property
  def capacity(self):
    return self._capacity

  @property
  def current(self):
    return self._current

  @property
  def remaining_sec(self):
    return self._remaining_sec
