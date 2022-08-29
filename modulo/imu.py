import redis
import json

class Imu():
  def __init__(self, redis):
    self.quaternion = self.Quaternion()
    self.linear_acceleration = self.LinearAcceleration()
    self.angular_velocity = self.AngularVelocity()
    self.magnetic_field = self.MagneticField()
    self.atmospheric_pressure = None
    self._heading = None

    pubsub = redis.pubsub()
    pubsub.psubscribe(**{'imu_*': self._subscribe})
    # pubsub.subscribe(**{'imu_accelerometer': self.accelerometer.update})
    # pubsub.subscribe(**{'imu_gyroscope': self.gyroscope.update})
    # pubsub.subscribe(**{'imu_compass': self.compass.update})
    thread = pubsub.run_in_thread(sleep_time=0.001)
    
  def _subscribe(self, message):
    if message['channel'] == b'imu_quaternion':
      self.quaternion._update(message['data'])
    elif message['channel'] == b'imu_linear_acceleration':
      self.linear_acceleration._update(message['data'])
    elif message['channel'] == b'imu_angular_velocity':
      self.angular_velocity._update(message['data'])
    elif message['channel'] == b'imu_magnetic_field':
      self.magnetic_field._update(message['data'])
    elif message['channel'] == b'imu_atmospheric_pressure':
      self.atmospheric_pressure = float(message['data'])
    elif message['channel'] == b'imu_heading':
      self._heading = float(message['data'])
  
  class Quaternion():
    def __init__(self):
      self._x, self._y, self._z, self._w = None, None, None, None
    
    def _update(self, message):
      data = json.loads(message.decode('utf8').replace("'", '"'))
      self._x = data['x']
      self._y = data['y']
      self._z = data['z']
      self._w = data['w']
    
    @property
    def dict(self):
      return{'x': self._x, 'y': self._y, 'z': self._z, 'w': self._w}

    @property
    def x(self):
      return self._x

    @property
    def y(self):
      return self._y

    @property
    def z(self):
      return self._z

    @property
    def w(self):
      return self._w

  class LinearAcceleration():
    def __init__(self):
      self._x, self._y, self._z = None, None, None
    
    def _update(self, message):
      data = json.loads(message.decode('utf8').replace("'", '"'))
      self._x = data['x']
      self._y = data['y']
      self._z = data['z']
    
    @property
    def dict(self):
      return{'x': self._x, 'y': self._y, 'z': self._z}

    @property
    def x(self):
      return self._x

    @property
    def y(self):
      return self._y

    @property
    def z(self):
      return self._z

  class AngularVelocity():
    def __init__(self):
      self._x, self._y, self._z = None, None, None
    
    def _update(self, message):
      data = json.loads(message.decode('utf8').replace("'", '"'))
      self._x = data['x']
      self._y = data['y']
      self._z = data['z']
    
    @property
    def dict(self):
      return{'x': self._x, 'y': self._y, 'z': self._z}

    @property
    def x(self):
      return self._x

    @property
    def y(self):
      return self._y

    @property
    def z(self):
      return self._z

  class MagneticField():
    def __init__(self):
      self._x, self._y, self._z = None, None, None
    
    def _update(self, message):
      data = json.loads(message.decode('utf8').replace("'", '"'))
      self._x = data['x']
      self._y = data['y']
      self._z = data['z']
    
    @property
    def dict(self):
      return{'x': self._x, 'y': self._y, 'z': self._z}

    @property
    def x(self):
      return self._x

    @property
    def y(self):
      return self._y

    @property
    def z(self):
      return self._z

  @property
  def heading(self):
    return self._heading