import redis

class Motor():
  def __init__(self, redis):
    self.redis = redis

  
  def __validate(self, speed):
    # If not number
    try:
      speed = float(speed)
    except ValueError:
      raise TypeError('`speed` must be a number.')

    # If not in range
    if not (-1 <= speed <= 1):
      raise ValueError('`speed` must be within -1 and 1.')

  def left(self, speed):
    try:
      self.__validate(speed)
    except Exception as error:
      raise error
    self.redis.publish('motor_left', speed)

  def right(self, speed):
    try:
      self.__validate(speed)
    except Exception as error:
      raise error
    self.redis.publish('motor_right', speed)

  def reset_pos(self):
    self.redis.publish('motor_reset_pos', 1)
    